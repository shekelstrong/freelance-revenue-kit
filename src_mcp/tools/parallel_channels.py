"""parallel_channels: параллельные каналы дохода."""


# Каналы с payout frequency
CHANNELS = {
    "kwork": {
        "payout_days": "Tue + Fri",
        "min_withdrawal_rub": 100,
        "commission": 5,
        "categories": "IT, дизайн, текст, маркетинг",
        "competition": "high",
        "time_to_first_payout": "1-7 days",
    },
    "fl_ru": {
        "payout_days": "weekly (пятница)",
        "min_withdrawal_rub": 150,
        "commission": 5,
        "categories": "IT, дизайн, текст",
        "competition": "high",
        "time_to_first_payout": "3-14 days",
    },
    "plati_ru": {
        "payout_days": "instant (webmoney / USDT / карта)",
        "min_withdrawal_rub": 0,
        "commission": 5,
        "categories": "Цифровые товары, аккаунты, ключи",
        "competition": "medium",
        "time_to_first_payout": "instant",
    },
    "lolzteam": {
        "payout_days": "instant (crypto)",
        "min_withdrawal_rub": 0,
        "commission": 3,
        "categories": "Цифровые товары, аккаунты, услуги, крипта",
        "competition": "medium",
        "time_to_first_payout": "1-3 days",
    },
    "tenchat": {
        "payout_days": "manual (через заказчика)",
        "min_withdrawal_rub": 0,
        "commission": 0,
        "categories": "B2B-услуги, консалтинг",
        "competition": "low",
        "time_to_first_payout": "7-30 days",
    },
    "upwork": {
        "payout_days": "weekly",
        "min_withdrawal_rub": 0,
        "commission": 10,
        "categories": "International IT",
        "competition": "high",
        "time_to_first_payout": "14-30 days",
    },
}


async def run(main_channel: str = "kwork", payout_frequency: str = "weekly") -> dict:
    """Стратегия параллельных каналов.

    Args:
        main_channel: Основной канал.
        payout_frequency: weekly / daily / instant.

    Returns:
        Словарь со стратегией.
    """
    channels = {k: v for k, v in CHANNELS.items()}

    # Приоритизация по payout frequency
    priority = []
    if payout_frequency == "instant":
        priority = ["plati_ru", "lolzteam", "kwork", "fl_ru", "tenchat", "upwork"]
    elif payout_frequency == "daily":
        priority = ["lolzteam", "kwork", "fl_ru", "plati_ru", "tenchat", "upwork"]
    else:  # weekly
        priority = ["kwork", "fl_ru", "lolzteam", "plati_ru", "tenchat", "upwork"]

    # Главный канал — первым
    if main_channel in priority:
        priority.remove(main_channel)
        priority.insert(0, main_channel)

    return {
        "main_channel": main_channel,
        "payout_frequency": payout_frequency,
        "prioritized_channels": [
            {"name": ch, "rank": i + 1, **channels[ch]} for i, ch in enumerate(priority)
        ],
        "strategy": [
            "Параллельная работа: 60% времени на main + 40% на второй канал",
            "Один канал не кормит — 3 канала = стабильный доход",
            "Разные payout days = деньги каждую неделю",
            "Crypto (Plati, Lolz) для моментальных выплат, fiat (Kwork) для основного",
        ],
        "synergy": {
            "kwork + plati": "Kwork приводит клиентов, Plati продаёт цифровые товары 24/7",
            "kwork + tenchat": "Kwork для быстрого cash, TenChat для долгосрочных B2B",
            "lolz + tenchat": "Lolz для быстрого cash, TenChat для построения личного бренда",
        },
    }
