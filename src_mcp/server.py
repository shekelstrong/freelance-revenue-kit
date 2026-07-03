"""Freelance Revenue Kit MCP Server."""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from src_mcp.tools import plan_first_revenue, parallel_channels, emergency_strategy, revenue_tracker


app = Server("freelance-revenue-kit")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="plan_first_revenue",
            description="План: от 0 до первого дохода за 7 дней. Стратегия по дням.",
            inputSchema={
                "type": "object",
                "properties": {
                    "skill": {"type": "string", "description": "Что умеешь"},
                    "current_savings_days": {"type": "integer", "default": 30, "description": "Сколько дней на деньгах"},
                },
                "required": ["skill"],
            },
        ),
        Tool(
            name="parallel_channels",
            description="Параллельные каналы дохода: Kwork + Plati + LolzTeam + TenChat.",
            inputSchema={
                "type": "object",
                "properties": {
                    "main_channel": {"type": "string", "default": "kwork"},
                    "payout_frequency": {"type": "string", "default": "weekly"},
                },
                "required": ["main_channel"],
            },
        ),
        Tool(
            name="emergency_strategy",
            description="Экстренные стратегии когда деньги нужны сегодня: перепродажа, услуги, крипта.",
            inputSchema={
                "type": "object",
                "properties": {
                    "amount_needed_rub": {"type": "integer", "description": "Сколько нужно"},
                    "deadline_days": {"type": "integer", "default": 3},
                },
                "required": ["amount_needed_rub"],
            },
        ),
        Tool(
            name="revenue_tracker",
            description="Трекер доходов: расчёт ROI по каналам, приоритизация, метрики.",
            inputSchema={
                "type": "object",
                "properties": {
                    "channels": {"type": "array", "items": {"type": "object"}, "description": "[{name, revenue, time_spent_hours}]"},
                },
                "required": ["channels"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    import json
    tools_map = {
        "plan_first_revenue": plan_first_revenue,
        "parallel_channels": parallel_channels,
        "emergency_strategy": emergency_strategy,
        "revenue_tracker": revenue_tracker,
    }
    try:
        result = await tools_map[name].run(**arguments)
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {type(e).__name__}: {e}")]


async def main():
    async with stdio_server() as (rs, ws):
        await app.run(rs, ws, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
