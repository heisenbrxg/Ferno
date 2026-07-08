import json
slides = [
    ("peer review.webp", "Peer Review"),
    ("residential.jpg", "Residential"),
    ("royal house chapel.jpg", "Royal House Chapel"),
    ("cinemas.avif", "Cinemas"),
    ("educational institutions.jpg", "Educational Institutions"),
    ("conventional centers.jpg", "Convention Centers"),
    ("labs.jpg", "Labs"),
    ("Hospital.jpg", "Hospital"),
    ("entertainment.avif", "Entertainment"),
    ("Supermarket and malls.webp", "Supermarket & Malls"),
    ("hospitality.avif", "Hospitality"),
    ("commercial building.jpg", "Commercial Building"),
    ("clean room.webp", "Clean Room"),
    ("paper mill'.webp", "Paper Mill"),
    ("cement factory.jpg", "Cement Factory"),
    ("paint shop.jpeg", "Paint Shop"),
    ("textile (2).jpg", "Textile"),
    ("textile.jpg", "Textile"),
    ("automobile.avif", "Automobile"),
    ("industrial.jpg", "Industrial"),
    ("flextronics-projects.jpg", "Flextronics Projects"),
    ("capgemini-karapakkam-chennai-computer-software-developers-2cdlglb.avif", "Capgemini"),
    ("Fbd6w3QaMAEpiEd.jpg", "Tech Park"),
    ("Data center.jpg", "Data Center"),
    ("Food industry.jpg", "Food Industry")
]

template = """<div class="swiper-slide gt-brand-slide-element">
    <div class="thumb" style="position: relative;">
        <svg xmlns="http://www.w3.org/2000/svg" width="384" height="278" viewBox="0 0 384 278">
            <defs>
                <pattern id="heroThumbPattern_{i}" patternUnits="objectBoundingBox" width="1" height="1">
                    <image href="./assets/img/{file}" width="384" height="278" preserveAspectRatio="xMidYMid slice" />
                </pattern>
            </defs>
            <path d="M4.29862 55.937C-7.17646 29.5206 12.1856 0 40.9866 0H294.194C309.385 0 323.266 8.60601 330.021 22.2133L379.17 121.213C384.733 132.419 384.733 145.581 379.17 156.787L330.021 255.787C323.266 269.394 309.385 278 294.194 278H40.9866C12.1855 278 -7.17646 248.479 4.29861 222.063L33.4576 154.937C37.8736 144.771 37.8736 133.229 33.4576 123.063L4.29862 55.937Z" fill="url(#heroThumbPattern_{i})" />
        </svg>
        <div class="hero-slide-title" style="position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%); background: rgba(10,10,10,0.85); color: #C9F31D; padding: 6px 16px; border-radius: 30px; font-weight: 700; font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase; white-space: nowrap; border: 1px solid rgba(201,243,29,0.3); pointer-events: none;">{title}</div>
    </div>
</div>
"""

out = ""
for i, (file, title) in enumerate(slides):
    out += template.format(i=i, file=file, title=title)

with open('output_slides.html', 'w', encoding='utf-8') as f:
    f.write(out)
