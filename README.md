# freelance-revenue-kit

> MCP-сервер: стратегии дохода фрилансера. Первый доход за 7 дней, параллельные каналы (Kwork + Plati + LolzTeam + TenChat), экстренные стратегии, ROI-трекер.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![MCP](https://img.shields.io/badge/MCP-compatible-purple.svg)](https://modelcontextprotocol.io)

## 🎯 Что это

MCP-сервер с 4 инструментами для дохода:

- 💰 **plan_first_revenue** — план: от 0 до первого дохода за 7 дней
- 🔀 **parallel_channels** — параллельные каналы (Kwork + Plati + LolzTeam)
- 🚨 **emergency_strategy** — экстренные стратегии (3 дня до cash)
- 📊 **revenue_tracker** — ROI по каналам, приоритизация

## 📦 Установка

```bash
git clone https://github.com/shekelstrong/freelance-revenue-kit.git
cd freelance-revenue-kit
pip install -r requirements.txt
```

## 🛠 MCP Tools

### plan_first_revenue
```python
result = await plan_first_revenue.run("Python-разработка", current_savings_days=15)
# → {urgency: "high", week_plan: [day 1-7], first_revenue_targets: {...}}
```

7-дневный план: создать кворки → откликнуться на 20 заказов → outreach → портфолио → повтор → пост → первый заказ.

### parallel_channels
```python
result = await parallel_channels.run(main_channel="kwork", payout_frequency="instant")
# → {prioritized_channels: [{name, rank, payout_days, ...}], synergy: {...}}
```

6 каналов: kwork / fl_ru / plati_ru / lolzteam / tenchat / upwork.

### emergency_strategy
```python
result = await emergency_strategy.run(amount_needed_rub=10000, deadline_days=3)
# → {options: [5 стратегий], priority_for_3_days: [...]}
```

5 стратегий: перепродажа, Kwork за 400₽, крипто-арбитраж, AI-агент, outreach к знакомым.

### revenue_tracker
```python
result = await revenue_tracker.run([
    {"name": "Kwork", "revenue": 50000, "time_spent_hours": 40, "costs": 0},
    {"name": "Plati", "revenue": 20000, "time_spent_hours": 5, "costs": 10000},
])
# → {channels: [...], totals: {...}, recommendation: "..."}
```

ROI % + profit/hour по каждому каналу + рекомендация.

## 📁 Структура

```
freelance-revenue-kit/
├── README.md
├── LICENSE
├── SKILL.md
├── requirements.txt
├── src_mcp/
│   ├── server.py
│   └── tools/
│       ├── plan_first_revenue.py
│       ├── parallel_channels.py
│       ├── emergency_strategy.py
│       └── revenue_tracker.py
└── .github/workflows/ci.yml
```

## 💸 Каналы дохода (payout frequency)

| Канал | Payout | Комиссия | До первого |
|---|---|---|---|
| **Kwork** | Tue + Fri | 5% | 1-7 дней |
| **FL.ru** | Пт | 5% | 3-14 дней |
| **Plati.ru** | Instant (USDT/карта) | 5% | 1 день |
| **LolzTeam** | Instant (crypto) | 3% | 1-3 дня |
| **TenChat** | Manual | 0% | 7-30 дней |
| **Upwork** | Weekly | 10% | 14-30 дней |

## 📄 License

MIT © Vasiliy Nedopekin (shekelstrong)
