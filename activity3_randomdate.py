from datetime import datetime, timedelta
import random
start_date = datetime(2010, 1, 1)
end_date = datetime(2026, 4, 28)

delta = end_date - start_date
random_days = random.randint(0, delta.days)

random_date = start_date + timedelta(days=random_days)
print("Random Date:", random_date.strftime("%d-%m-%Y"))