from django.core.management.base import BaseCommand
from login.models import ChatbotQA


QA_DATA = [

    # ── THAILAND ────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Thailand",
        "answer": (
            "Thailand - Land of Smiles!\n\n"
            "Thailand is a Southeast Asian gem famous for its ornate temples, "
            "turquoise beaches, lush jungles, and vibrant street food scene. "
            "Top attractions include:\n"
            "- Bangkok: Grand Palace, Wat Pho, floating markets\n"
            "- Chiang Mai: ancient temples, elephant sanctuaries, night bazaar\n"
            "- Phuket & Krabi: stunning beaches and island hopping\n"
            "- Pattaya: nightlife and water sports\n\n"
            "Best time to visit: November to April (cool & dry season).\n"
            "Currency: Thai Baht (THB). Language: Thai.\n"
            "Known for: Pad Thai, Tom Yum soup, and world-class hospitality."
        ),
    },
    {
        "question": "Thailand package",
        "answer": (
            "Our Thailand packages start from Rs. 35,000 per person and cover:\n"
            "- Hotel accommodation (3 to 7 nights)\n"
            "- Bangkok + Phuket itinerary\n"
            "- Temple tours, beach excursions & street food walks\n"
            "- Airport transfers included\n\n"
            "Visit the Packages page to see current prices and book your Thailand trip!"
        ),
    },

    # ── MALDIVES ────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Maldives",
        "answer": (
            "Maldives - Paradise on Earth!\n\n"
            "The Maldives is an Indian Ocean archipelago of 26 coral atolls known for "
            "its crystal-clear lagoons, overwater bungalows, and spectacular marine life. "
            "Highlights include:\n"
            "- Overwater villas with direct ocean access\n"
            "- Snorkelling & scuba diving with manta rays and whale sharks\n"
            "- Sandbank picnics and sunset cruises\n"
            "- Bioluminescent beach at Vaadhoo Island\n\n"
            "Best time to visit: November to April (dry season).\n"
            "Currency: Maldivian Rufiyaa (MVR). Language: Dhivehi / English.\n"
            "Perfect for: Honeymoons, anniversaries & luxury escapes."
        ),
    },
    {
        "question": "Maldives package",
        "answer": (
            "Our Maldives packages include:\n"
            "- Overwater or beach villa stay (4 to 7 nights)\n"
            "- All-inclusive meals at the resort\n"
            "- Snorkelling, diving & water sports\n"
            "- Speedboat or seaplane transfers\n\n"
            "Prices start from Rs. 65,000 per person. Check the Packages page for details!"
        ),
    },

    # ── PARIS ───────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Paris",
        "answer": (
            "Paris - The City of Light!\n\n"
            "Paris is the capital of France and one of the world's most visited cities, "
            "celebrated for its art, fashion, gastronomy, and culture. Must-sees:\n"
            "- Eiffel Tower: iconic iron lattice tower\n"
            "- Louvre Museum: home of the Mona Lisa\n"
            "- Notre-Dame Cathedral & Sacre-Coeur\n"
            "- Champs-Elysees & Arc de Triomphe\n"
            "- Seine River cruises & Versailles day trip\n\n"
            "Best time to visit: April to June or September to November.\n"
            "Currency: Euro (EUR). Language: French.\n"
            "Famous for: Croissants, wine, high fashion & romance."
        ),
    },
    {
        "question": "Paris package",
        "answer": (
            "Our Paris packages start from Rs. 80,000 per person and include:\n"
            "- 5 to 7 nights in a centrally located hotel\n"
            "- Eiffel Tower skip-the-line tickets\n"
            "- Louvre Museum guided tour\n"
            "- Seine River dinner cruise\n"
            "- Versailles day excursion\n\n"
            "Browse the Packages page to find the right Paris package for you!"
        ),
    },

    # ── BALI ────────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Bali",
        "answer": (
            "Bali - Island of the Gods!\n\n"
            "Bali is an Indonesian island renowned for its forested volcanic mountains, "
            "iconic rice paddies, beaches, and coral reefs. Top spots:\n"
            "- Ubud: cultural heart, rice terraces & monkey forest\n"
            "- Seminyak & Kuta: beach clubs and nightlife\n"
            "- Tanah Lot & Uluwatu temples (stunning cliff-top views)\n"
            "- Mount Batur: sunrise trekking\n"
            "- Nusa Penida: cliffside views & manta ray diving\n\n"
            "Best time to visit: April to October (dry season).\n"
            "Currency: Indonesian Rupiah (IDR). Language: Bahasa Indonesia / Balinese.\n"
            "Famous for: Yoga retreats, spa culture & traditional dance."
        ),
    },
    {
        "question": "Bali package",
        "answer": (
            "Our Bali packages start from Rs. 30,000 per person and cover:\n"
            "- 5 to 7 nights in a villa or resort\n"
            "- Ubud cultural tour & rice terrace visit\n"
            "- Temple visits (Tanah Lot, Uluwatu)\n"
            "- Mount Batur sunrise trek\n"
            "- Airport transfers included\n\n"
            "Visit the Packages page to see current Bali deals!"
        ),
    },

    # ── DUBAI ───────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Dubai",
        "answer": (
            "Dubai - City of the Future!\n\n"
            "Dubai is a glittering metropolis in the UAE famous for record-breaking "
            "architecture, luxury shopping, and desert adventures. Highlights:\n"
            "- Burj Khalifa: world's tallest building (observation deck)\n"
            "- Dubai Mall & Dubai Fountain show\n"
            "- Palm Jumeirah & Atlantis resort\n"
            "- Desert safari with dune bashing, camel rides & BBQ dinner\n"
            "- Dubai Creek & old gold/spice souks\n"
            "- Burj Al Arab: iconic luxury hotel\n\n"
            "Best time to visit: November to March (pleasant weather).\n"
            "Currency: UAE Dirham (AED). Language: Arabic / English.\n"
            "Famous for: Luxury, shopping, and modern marvels."
        ),
    },
    {
        "question": "Dubai package",
        "answer": (
            "Our Dubai packages start from Rs. 45,000 per person and include:\n"
            "- 4 to 6 nights in a 4/5-star hotel\n"
            "- Burj Khalifa At the Top ticket\n"
            "- Desert safari with BBQ dinner\n"
            "- Dhow cruise dinner\n"
            "- City tour & Dubai Mall visit\n\n"
            "Check the Packages page to book your Dubai adventure!"
        ),
    },

    # ── SWITZERLAND ─────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Switzerland",
        "answer": (
            "Switzerland - Land of Alps & Chocolate!\n\n"
            "Switzerland is a landlocked Central European country celebrated for its "
            "snow-capped mountains, pristine lakes, and precision craftsmanship. Top sights:\n"
            "- Interlaken: adventure capital (skydiving, paragliding)\n"
            "- Jungfraujoch: 'Top of Europe' at 3,454 m altitude\n"
            "- Lucerne: Chapel Bridge & Lake Lucerne cruise\n"
            "- Zurich: vibrant city, art museums & nightlife\n"
            "- Zermatt & the Matterhorn: skiing & scenic trains\n"
            "- Montreux: Chillon Castle on Lake Geneva\n\n"
            "Best time to visit: June to September (summer) or December to February (skiing).\n"
            "Currency: Swiss Franc (CHF). Languages: German, French, Italian.\n"
            "Famous for: Swiss chocolate, cheese, watches & Alpine beauty."
        ),
    },
    {
        "question": "Switzerland package",
        "answer": (
            "Our Switzerland packages start from Rs. 1,10,000 per person and include:\n"
            "- 6 to 8 nights in 3/4-star hotels\n"
            "- Jungfraujoch excursion (Top of Europe)\n"
            "- Swiss Travel Pass for trains & buses\n"
            "- Lucerne & Interlaken guided tours\n"
            "- Rhine Falls visit\n\n"
            "Browse the Packages page for Switzerland itineraries!"
        ),
    },

    # ── SYDNEY ──────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Sydney",
        "answer": (
            "Sydney - Australia's Harbour City!\n\n"
            "Sydney is Australia's largest city, known for its stunning harbour, "
            "golden beaches, and iconic landmarks. Must-visit spots:\n"
            "- Sydney Opera House: UNESCO World Heritage Site\n"
            "- Harbour Bridge climb & BridgeClimb experience\n"
            "- Bondi Beach: surfing & coastal walks\n"
            "- Darling Harbour: dining & entertainment\n"
            "- Taronga Zoo with harbour views\n"
            "- Blue Mountains: Three Sisters rock formation\n\n"
            "Best time to visit: September to November or March to May.\n"
            "Currency: Australian Dollar (AUD). Language: English.\n"
            "Famous for: Surf culture, cafe scene & outdoor lifestyle."
        ),
    },
    {
        "question": "Sydney package",
        "answer": (
            "Our Sydney packages start from Rs. 95,000 per person and cover:\n"
            "- 6 to 8 nights hotel accommodation\n"
            "- Sydney Opera House & Harbour Bridge tour\n"
            "- Blue Mountains day trip\n"
            "- Bondi Beach guided walk\n"
            "- Airport transfers included\n\n"
            "Visit the Packages page to explore Sydney itineraries!"
        ),
    },

    # ── TOKYO ───────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Tokyo",
        "answer": (
            "Tokyo - Where Tradition Meets Technology!\n\n"
            "Tokyo, Japan's capital, is a neon-lit metropolis blending ultramodern "
            "and traditional elements. Key highlights:\n"
            "- Shibuya Crossing: world's busiest pedestrian scramble\n"
            "- Senso-ji Temple in Asakusa: Tokyo's oldest temple\n"
            "- Shinjuku: skyscrapers, Kabukicho & Golden Gai\n"
            "- Akihabara: electronics & anime culture\n"
            "- teamLab Borderless: immersive digital art museum\n"
            "- Day trip to Mount Fuji & Hakone\n\n"
            "Best time to visit: March to April (cherry blossoms) or October to November (autumn).\n"
            "Currency: Japanese Yen (JPY). Language: Japanese.\n"
            "Famous for: Sushi, ramen, anime, Bullet Train & cherry blossoms."
        ),
    },
    {
        "question": "Tokyo package",
        "answer": (
            "Our Tokyo packages start from Rs. 85,000 per person and include:\n"
            "- 6 to 8 nights in a central hotel\n"
            "- Senso-ji & Meiji Shrine guided tour\n"
            "- Shibuya, Shinjuku & Akihabara exploration\n"
            "- Mount Fuji day trip\n"
            "- JR Pass for bullet train rides\n\n"
            "Check the Packages page for full Tokyo itineraries!"
        ),
    },

    # ── INDONESIA ───────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Indonesia",
        "answer": (
            "Indonesia - The Emerald of the Equator!\n\n"
            "Indonesia is the world's largest archipelago with over 17,000 islands, "
            "featuring volcanoes, rainforests, and diverse cultures. Top destinations:\n"
            "- Bali: rice terraces, temples & beaches\n"
            "- Yogyakarta: Borobudur & Prambanan temples\n"
            "- Lombok: Rinjani volcano & pristine beaches\n"
            "- Komodo Island: Komodo dragons in the wild\n"
            "- Raja Ampat: world-class diving & marine life\n\n"
            "Best time to visit: May to September (dry season).\n"
            "Currency: Indonesian Rupiah (IDR). Language: Bahasa Indonesia.\n"
            "Famous for: Tropical beauty, batik textiles & rich spice heritage."
        ),
    },
    {
        "question": "Indonesia package",
        "answer": (
            "Our Indonesia packages start from Rs. 28,000 per person and include:\n"
            "- 5 to 7 nights accommodation\n"
            "- Bali & Yogyakarta combined itinerary\n"
            "- Borobudur temple sunrise tour\n"
            "- Beach & diving excursions\n"
            "- Domestic flights between islands\n\n"
            "Visit the Packages page to book your Indonesian adventure!"
        ),
    },

    # ── MALAYSIA ────────────────────────────────────────────────────────────────
    {
        "question": "Tell me about Malaysia",
        "answer": (
            "Malaysia - Truly Asia!\n\n"
            "Malaysia is a multicultural Southeast Asian nation offering rainforests, "
            "modern cities, and pristine islands. Key highlights:\n"
            "- Kuala Lumpur: Petronas Twin Towers, Batu Caves\n"
            "- Penang: UNESCO heritage town & famous street food\n"
            "- Langkawi: duty-free island with cable cars & beaches\n"
            "- Cameron Highlands: tea plantations & cool mountain air\n"
            "- Borneo: orangutans, rainforests & diving at Sipadan\n\n"
            "Best time to visit: December to February (west coast) or May to September (east coast).\n"
            "Currency: Malaysian Ringgit (MYR). Languages: Malay, English, Chinese, Tamil.\n"
            "Famous for: Nasi Lemak, Roti Canai & multicultural harmony."
        ),
    },
    {
        "question": "Malaysia package",
        "answer": (
            "Our Malaysia packages start from Rs. 25,000 per person and cover:\n"
            "- 5 to 7 nights in Kuala Lumpur & Langkawi\n"
            "- Petronas Twin Towers observation deck\n"
            "- Batu Caves & Penang heritage walk\n"
            "- Langkawi cable car & island hopping\n"
            "- Airport transfers included\n\n"
            "Check the Packages page to explore Malaysia deals!"
        ),
    },

    # ── GENERAL TRAVEL Q&A ───────────────────────────────────────────────────────
    {
        "question": "How do I book a package",
        "answer": (
            "Booking a package is simple!\n\n"
            "1. Browse our Packages page and find your dream destination.\n"
            "2. Click 'View More' to see full details.\n"
            "3. Click 'Book Now' and fill in your travel date.\n"
            "4. Enter your payment details to confirm the booking.\n"
            "5. You will receive a booking confirmation instantly!"
        ),
    },
    {
        "question": "What packages are available",
        "answer": (
            "We offer amazing travel packages to:\n"
            "Thailand, Maldives, Paris, Bali, Dubai, Switzerland, Sydney, Tokyo, Indonesia, Malaysia & more!\n\n"
            "Each package includes accommodation, guided tours, and transfers.\n"
            "Visit the Packages page or ask me about any specific destination for details!"
        ),
    },
    {
        "question": "Visa requirements",
        "answer": (
            "Visa requirements vary by destination and your passport:\n\n"
            "- Thailand: Visa on arrival for Indian passport holders (30 days).\n"
            "- Maldives: Visa on arrival (30 days, free).\n"
            "- Bali / Indonesia: Visa on arrival for Indians (30 days).\n"
            "- Malaysia: Visa on arrival for Indians (30 days) in most cases.\n"
            "- Dubai: Visa required; we assist with the process.\n"
            "- Paris & Switzerland: Schengen visa required for Indian citizens.\n"
            "- Sydney: Australian Tourist Visa (ETA) required.\n"
            "- Tokyo: Japanese Tourist Visa required for Indians.\n\n"
            "Contact our team for visa assistance and documentation support!"
        ),
    },
    {
        "question": "Best time to travel",
        "answer": (
            "Best travel seasons by destination:\n\n"
            "- Thailand: November to April\n"
            "- Maldives: November to April\n"
            "- Paris: April to June, September to November\n"
            "- Bali: April to October\n"
            "- Dubai: November to March\n"
            "- Switzerland: June to September (summer) or December to February (skiing)\n"
            "- Sydney: September to November and March to May\n"
            "- Tokyo: March to April (cherry blossoms) and October to November\n"
            "- Indonesia: May to September\n"
            "- Malaysia: December to February (west coast)\n\n"
            "Ask me about any specific spot for personalised travel advice!"
        ),
    },
    {
        "question": "Cancel booking",
        "answer": (
            "Cancellation Policy:\n\n"
            "- Cancellations made 7 or more days before the travel date: Full refund.\n"
            "- Cancellations within 3 to 7 days: 50% refund.\n"
            "- Cancellations within 48 hours: No refund.\n\n"
            "To cancel, go to My Bookings and click 'Cancel Booking', "
            "or contact our support team at support@smarttravel.com."
        ),
    },
    {
        "question": "Payment methods",
        "answer": (
            "We accept the following payment methods:\n\n"
            "- Credit / Debit Card (Visa, MasterCard, RuPay)\n"
            "- Net Banking\n"
            "- UPI (Google Pay, PhonePe, Paytm)\n"
            "- EMI options available on select packages\n\n"
            "All payments are secured with 256-bit SSL encryption."
        ),
    },
    {
        "question": "Contact support",
        "answer": (
            "You can reach our support team via:\n\n"
            "- Phone: 1800-123-4567 (Toll-free, Monday to Saturday, 9 AM to 6 PM)\n"
            "- Email: support@smarttravel.com\n"
            "- Live Chat: Available on this page via our Travel Assistant\n\n"
            "We are happy to help with bookings, visa queries, itinerary planning & more!"
        ),
    },
    {
        "question": "What is included in the package",
        "answer": (
            "Most of our packages include:\n\n"
            "- Hotel / resort accommodation\n"
            "- Airport transfers (pick-up & drop-off)\n"
            "- Guided sightseeing tours\n"
            "- Entrance fees to major attractions\n\n"
            "Some packages also include meals and domestic flights.\n"
            "Check the individual package details for a full breakdown!"
        ),
    },
    {
        "question": "Travel insurance",
        "answer": (
            "We strongly recommend travel insurance for all international trips.\n\n"
            "Our packages offer optional travel insurance covering:\n"
            "- Trip cancellation & interruption\n"
            "- Medical emergencies abroad\n"
            "- Lost or delayed baggage\n"
            "- Flight delays\n\n"
            "Add travel insurance at checkout for peace of mind on your journey!"
        ),
    },
]


class Command(BaseCommand):
    help = "Seeds the ChatbotQA table with travel destination Q&A data"

    def handle(self, *args, **kwargs):
        # Clear existing entries to avoid duplicates on re-run
        deleted_count, _ = ChatbotQA.objects.all().delete()
        self.stdout.write(f"Cleared {deleted_count} existing ChatbotQA entries.")

        # Bulk create new entries
        objs = [ChatbotQA(question=item["question"], answer=item["answer"]) for item in QA_DATA]
        ChatbotQA.objects.bulk_create(objs)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {len(objs)} ChatbotQA entries for travel destinations!"
            )
        )
