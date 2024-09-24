from .database import engine, SessionLocal
from .models import Base, Item
from apscheduler.schedulers.background import BackgroundScheduler
from .services.scraper import fetch_item_data


def update_prices():
    db = SessionLocal()
    items = db.query(Item).all()
    for item in items:
        data = fetch_item_data(item.url)
        item.price = data['price']
        db.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(update_prices, 'interval', hours=1)
scheduler.start()


Base.metadata.create_all(bind=engine)
