"""revenue_tracker: ROI по каналам."""


async def run(channels: list) -> dict:
    """Считает ROI каналов.

    Args:
        channels: [{name, revenue, time_spent_hours, costs}].

    Returns:
        Словарь с ROI.
    """
    if not channels:
        return {"error": "Empty channels list"}

    results = []
    total_revenue = 0
    total_time = 0
    total_costs = 0

    for ch in channels:
        name = ch.get("name", "?")
        revenue = ch.get("revenue", 0)
        time_h = ch.get("time_spent_hours", 0)
        costs = ch.get("costs", 0)
        profit = revenue - costs
        roi = (profit / costs * 100) if costs > 0 else float("inf")
        hourly = (profit / time_h) if time_h > 0 else 0

        results.append({
            "name": name,
            "revenue": revenue,
            "costs": costs,
            "profit": profit,
            "time_hours": time_h,
            "roi_pct": round(roi, 1) if roi != float("inf") else "∞",
            "hourly_profit_rub": round(hourly),
        })

        total_revenue += revenue
        total_time += time_h
        total_costs += costs

    # Сортировка по hourly profit
    results.sort(key=lambda x: -x["hourly_profit_rub"])

    # Рекомендация
    if results:
        best = results[0]
        worst = results[-1]
        recommendation = f"Масштабируй '{best['name']}' ({best['hourly_profit_rub']}₽/час). Сократи '{worst['name']}' ({worst['hourly_profit_rub']}₽/час)."
    else:
        recommendation = "Нет данных"

    return {
        "channels": results,
        "totals": {
            "revenue": total_revenue,
            "costs": total_costs,
            "profit": total_revenue - total_costs,
            "time_hours": total_time,
            "avg_hourly_profit": round((total_revenue - total_costs) / total_time) if total_time else 0,
        },
        "recommendation": recommendation,
    }
