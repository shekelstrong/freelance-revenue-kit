"""plan_first_revenue: план от 0 до первого дохода за 7 дней."""


async def run(skill: str, current_savings_days: int = 30) -> dict:
    """План первого дохода.

    Args:
        skill: Что умеешь.
        current_savings_days: Сколько дней runway.

    Returns:
        Словарь с планом по дням.
    """
    urgency = "critical" if current_savings_days < 14 else "high" if current_savings_days < 30 else "normal"

    return {
        "skill": skill,
        "urgency": urgency,
        "current_savings_days": current_savings_days,
        "week_plan": [
            {"day": 1, "task": "Создать 3-5 кворков на Kwork. Минимум один за 400₽ (минимум).", "deliverable": "5 кворков опубликованы"},
            {"day": 2, "task": "Откликнуться на 20 заказов в бирже Kwork. Короткие сообщения.", "deliverable": "20 откликов"},
            {"day": 3, "task": "Outreach: 10 DM в TenChat / VC.ru / Telegram-чатах фрилансеров.", "deliverable": "10 личных сообщений"},
            {"day": 4, "task": "Создать портфолио-демо (если нет). 3-5 проектов в GitHub.", "deliverable": "README + 3-5 репо"},
            {"day": 5, "task": "Повторить день 2-3 с лучшими формулировками (на основе фидбека).", "deliverable": "20 новых откликов"},
            {"day": 6, "task": "Опубликовать пост в TenChat / VC.ru: кейс или инструкция.", "deliverable": "Пост опубликован"},
            {"day": 7, "task": "Первый заказ (если не пришёл — повторить день 5).", "deliverable": "1 оплата получена"},
        ],
        "first_revenue_targets": {
            "kwork": {"min": 400, "realistic": 1000, "good": 5000, "payout": "Tue + Fri"},
            "fl_ru": {"min": 500, "realistic": 2000, "good": 10000, "payout": "weekly"},
            "upwork": {"min": 50, "realistic": 200, "good": 1000, "payout": "weekly"},
            "freelancerhunt": {"min": 500, "realistic": 1500, "good": 8000, "payout": "manual"},
        },
        "principles": [
            "Первый заказ важнее идеального заказа",
            "Минимум усилий → первый доход → петля обратной связи → улучшение",
            "10 откликов в день = 1-2 заказа в неделю статистически",
            "Не жди 'идеального портфолио' — сделай на коленке и иди",
            "Самозанятость открывается за 5 минут через nalog.ru",
        ],
        "anti_patterns": [
            "Ждать пока 'всё будет готово' — 80% кворков создаются за 1 вечер",
            "Идеальный дизайн портфолио — текст + скриншоты в Notion быстрее",
            "Один канал дохода — Kwork платит 2 раза в неделю (вт/пт)",
        ],
    }
