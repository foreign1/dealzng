from datetime import datetime
from . models import ShopItem, CategoryChoices
from . import db

# Function to add the data to the database
def run_migrations():
    db.create_all()
    for data in dummy_data:
        item = ShopItem(
            name=data['name'],
            category=CategoryChoices[data['category'].upper()],
            desc_short=data['desc_short'],
            desc_long=data['desc_long'],
            price=data['price'],
            discount_price=data['discount_price'],
            time_created=data['time_created']
        )
        db.session.add(item)
    db.session.commit()

dummy_data = [
    {"name": "Personal Training Session", "category": CategoryChoices.TRAINING, "desc_short": "A one-on-one training session with a certified personal trainer", "desc_long": "This personalized training session is tailored to your specific fitness goals and needs. Our certified personal trainers will work with you to create a customized workout plan that will help you achieve your desired results.", "price": 30000.00, "discount_price": 25000.00, "time_created": datetime.utcnow()},
    {"name": "Luxury Hotel Suite", "category": CategoryChoices.HOTEL, "desc_short": "A luxurious hotel suite with stunning views and amenities", "desc_long": "Experience the ultimate in luxury with our hotel suite package. Enjoy stunning views, world-class amenities, and exceptional service from our friendly and knowledgeable staff.", "price": 150000.00, "discount_price": 120000.00, "time_created": datetime.utcnow()},
    {"name": "Round-Trip Airfare to Paris", "category": CategoryChoices.TRAVEL, "desc_short": "A round-trip ticket to Paris, France", "desc_long": "Discover the City of Light with our round-trip airfare package. Experience the romance and charm of Paris with its world-renowned cuisine, art, and culture.", "price": 240000.00, "discount_price": 210000.00, "time_created": datetime.utcnow()},
    {"name": "Spa Day Package", "category": CategoryChoices.SPA, "desc_short": "A full day of relaxation and rejuvenation at our spa", "desc_long": "Treat yourself to a day of pampering and relaxation with our spa day package. Enjoy a full range of services, including massages, facials, and body treatments, all designed to leave you feeling refreshed and rejuvenated.", "price": 60000.00, "discount_price": 50000.00, "time_created": datetime.utcnow()},
    {"name": "Gourmet Dinner for Two", "category": CategoryChoices.RESTAURANT, "desc_short": "A romantic dinner for two at our award-winning restaurant", "desc_long": "Indulge in a culinary experience unlike any other with our gourmet dinner for two. Enjoy a multi-course meal prepared by our award-winning chef, paired with the finest wines from around the world.", "price": 50000.00, "discount_price": 40000.00, "time_created": datetime.utcnow()},
    {"name": "Luxury Hotel Suite", "category": CategoryChoices.HOTEL, "desc_short": "A luxurious hotel suite with stunning views and amenities", "desc_long": "Experience the ultimate in luxury with our hotel suite package. Enjoy stunning views, world-class amenities, and exceptional service from our friendly and knowledgeable staff.", "price": 80000.00, "discount_price": 70000.00, "time_created": datetime.utcnow()},
    {"name": "Relaxing Swedish Massage", "category": CategoryChoices.SPA, "desc_short": "A calming Swedish massage to soothe your senses", "desc_long": "Indulge in a relaxing Swedish massage that is designed to reduce stress and tension. Our skilled therapists will use long, smooth strokes to ease muscle soreness and promote relaxation.", "price": 20000.00, "discount_price": 17000.00, "time_created": datetime.utcnow()},
    {"name": "Five-Course Tasting Menu", "category": CategoryChoices.RESTAURANT, "desc_short": "A five-course tasting menu featuring the chef's signature dishes", "desc_long": "Savor the flavors of our chef's signature dishes with our five-course tasting menu. Each dish is carefully crafted using the freshest ingredients, and is designed to take your taste buds on a culinary journey.", "price": 45000.00, "discount_price": 38000.00, "time_created": datetime.utcnow()},
    {"name": "Private Jet Charter", "category": CategoryChoices.TRAVEL, "desc_short": "A private jet charter to your dream destination", "desc_long": "Travel in style and comfort with our private jet charter service. Fly to your dream destination in a luxurious private jet, complete with all the amenities you need to make your journey as comfortable as possible.", "price": 90000.00, "discount_price": 85000.00, "time_created": datetime.utcnow()},
    {"name": "Yoga Class Package", "category": CategoryChoices.TRAINING, "desc_short": "A package of 10 yoga classes with our certified instructors", "desc_long": "Achieve inner peace and balance with our package of 10 yoga classes. Our certified instructors will guide you through each pose, helping you improve your flexibility, strength, and mindfulness.", "price": 20000.00, "discount_price": 15000.00, "time_created": datetime.utcnow()},
    {"name": "Couples Spa Retreat", "category": CategoryChoices.SPA, "desc_short": "A romantic spa retreat for couples", "desc_long": "Escape the stresses of daily life with our couples spa retreat. Enjoy a day of pampering and relaxation with your partner, and experience a range of spa treatments designed to rejuvenate your mind, body, and soul.", "price": 120000.00, "discount_price": 100000.00, "time_created": datetime.utcnow()},
    {
        "name": "Weekend Getaway Package", 
        "category": CategoryChoices.HOTEL, 
        "desc_short": "A weekend getaway package at our luxury hotel", 
        "desc_long": "Enjoy a luxurious weekend getaway at our hotel, complete with stunning views, world-class amenities, and exceptional service. Take advantage of our special package deal, which includes accommodations, meals, and a range of activities.", 
        "price": 1050000.00, 
        "discount_price": 1000000.00, 
        "time_created": datetime.utcnow()
    },
    {
        "name": "Private Tennis Lesson",
        "category": CategoryChoices.TRAINING,
        "desc_short": "One-on-one tennis lesson with a certified instructor",
        "desc_long": "Improve your tennis skills with a private lesson tailored to your needs. Our certified instructors will work with you to develop a personalized training plan to help you reach your full potential.",
        "price": 100000.00,
        "discount_price": 90000.00,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Beachfront Villa",
        "category": "hotel",
        "desc_short": "Luxury beachfront villa with stunning ocean views",
        "desc_long": "Experience the ultimate in luxury with our beachfront villa package. Enjoy stunning ocean views, world-class amenities, and exceptional service from our friendly and knowledgeable staff.",
        "price": 700000.00,
        "discount_price": 670000.00,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Adventure Tour Package",
        "category": "travel",
        "desc_short": "An adrenaline-filled adventure tour package",
        "desc_long": "Experience the thrill of adventure with our tour package. Explore remote destinations and participate in activities like hiking, kayaking, and zip-lining, all while being accompanied by experienced guides.",
        "price": 14990.00,
        "discount_price": 11990.00,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Deep Tissue Massage",
        "category": "spa",
        "desc_short": "A deep tissue massage to release tension",
        "desc_long": "Unwind with a deep tissue massage designed to release chronic muscle tension. Our skilled therapists will use deep pressure and slow strokes to help you relax and alleviate muscle soreness.",
        "price": 12900.99,
        "discount_price": 10000.99,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Chef's Tasting Menu",
        "category": "restaurant",
        "desc_short": "A six-course tasting menu featuring the chef's signature dishes",
        "desc_long": "Savor the flavors of our chef's signature dishes with our six-course tasting menu. Each dish is carefully crafted using the freshest ingredients and is designed to take your taste buds on a culinary journey.",
        "price": 24900.99,
        "discount_price": 19900.99,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Penthouse Suite",
        "category": "hotel",
        "desc_short": "A luxurious penthouse suite with breathtaking city views",
        "desc_long": "Experience the ultimate in luxury with our penthouse suite package. Enjoy breathtaking city views, world-class amenities, and exceptional service from our friendly and knowledgeable staff.",
        "price": 14990.99,
        "discount_price": 11990.99,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Hot Air Balloon Ride",
        "category": "travel",
        "desc_short": "A scenic hot air balloon ride with panoramic views",
        "desc_long": "Take to the skies with our hot air balloon ride package. Enjoy breathtaking panoramic views as you soar over stunning",
        "price": 14995.99,
        "discount_price": 11995.99,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Penthouse Suite",
        "category": "hotel",
        "desc_short": "A mega-luxurious penthouse suite with breathtaking city views",
        "desc_long": "Experience the ultimate in luxury with our mega-penthouse suite package. Enjoy breathtaking city views, world-class amenities, and exceptional service from our friendly and knowledgeable staff.",
        "price": 14990.99,
        "discount_price": 11990.99,
        "time_created": datetime.utcnow()
    },
    {
        "name": "Cold Air Balloon Drop",
        "category": "travel",
        "desc_short": "A scenic cold air balloon drop with panoramic views",
        "desc_long": "Drop from the skies with our hot air balloon ride package. Enjoy breathtaking panoramic views as you soar over stunning",
        "price": 14999.99,
        "discount_price": 11999.99,
        "time_created": datetime.utcnow()
    }
]

