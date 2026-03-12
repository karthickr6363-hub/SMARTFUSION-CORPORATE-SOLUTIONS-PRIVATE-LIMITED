import re
import codecs

# 1. Update HTML
html_path = r"how-it-works.html"
with codecs.open(html_path, 'r', 'utf-8') as f:
    html = f.read()

new_section = r"""    <!-- How It Works Start -->
    <div class="container-fluid py-5 wow fadeInUp" data-wow-delay="0.1s" style="overflow-x: hidden;">
        <div class="container py-5">
            <div class="section-title text-center position-relative pb-3 mb-5 mx-auto" style="max-width: 600px;">
                <h5 class="fw-bold text-primary text-uppercase">Process</h5>
                <h1 class="mb-0">How It Works</h1>
            </div>
            
            <!-- Step 1 -->
            <div class="row g-5 align-items-center mb-5 process-row">
                <div class="col-lg-6 wow slideInLeft" data-wow-delay="0.1s">
                    <div class="process-img-wrapper position-relative h-100">
                        <img class="img-fluid rounded shadow-lg float-anim" src="img/about.jpg" alt="Consultation" style="width: 100%; height: 400px; object-fit: cover;">
                        <div class="process-number-badge">1</div>
                    </div>
                </div>
                <div class="col-lg-6 wow slideInRight" data-wow-delay="0.3s">
                    <h2 class="mb-4">Consultation</h2>
                    <p class="mb-4 fs-5 text-muted">We begin by understanding your specific business needs and goals through an in-depth discussion and analysis. Our experts take the time to learn your vision.</p>
                </div>
            </div>
            
            <!-- Step 2 -->
            <div class="row g-5 align-items-center mb-5 process-row flex-lg-row-reverse">
                <div class="col-lg-6 wow slideInRight" data-wow-delay="0.1s">
                    <div class="process-img-wrapper position-relative h-100">
                        <img class="img-fluid rounded shadow-lg float-anim-reverse" src="img/feature.jpg" alt="Planning" style="width: 100%; height: 400px; object-fit: cover;">
                        <div class="process-number-badge left-badge">2</div>
                    </div>
                </div>
                <div class="col-lg-6 wow slideInLeft" data-wow-delay="0.3s">
                    <h2 class="mb-4">Planning & Strategy</h2>
                    <p class="mb-4 fs-5 text-muted">Our experts craft a tailored strategy and project plan designed to deliver optimal results efficiently, setting the roadmap for success.</p>
                </div>
            </div>
            
            <!-- Step 3 -->
            <div class="row g-5 align-items-center mb-5 process-row">
                <div class="col-lg-6 wow slideInLeft" data-wow-delay="0.1s">
                    <div class="process-img-wrapper position-relative h-100">
                        <img class="img-fluid rounded shadow-lg float-anim" src="img/carousel-1.jpg" alt="Execution" style="width: 100%; height: 400px; object-fit: cover;">
                        <div class="process-number-badge">3</div>
                    </div>
                </div>
                <div class="col-lg-6 wow slideInRight" data-wow-delay="0.3s">
                    <h2 class="mb-4">Execution & Delivery</h2>
                    <p class="mb-4 fs-5 text-muted">We implement the proposed solutions with precision, ensuring high quality and timely delivery of the project using agile methodologies.</p>
                </div>
            </div>
            
            <!-- Step 4 -->
            <div class="row g-5 align-items-center mb-5 process-row flex-lg-row-reverse">
                <div class="col-lg-6 wow slideInRight" data-wow-delay="0.1s">
                    <div class="process-img-wrapper position-relative h-100">
                        <img class="img-fluid rounded shadow-lg float-anim-reverse" src="img/carousel-2.jpg" alt="Testing" style="width: 100%; height: 400px; object-fit: cover;">
                        <div class="process-number-badge left-badge">4</div>
                    </div>
                </div>
                <div class="col-lg-6 wow slideInLeft" data-wow-delay="0.3s">
                    <h2 class="mb-4">Testing & Q/A</h2>
                    <p class="mb-4 fs-5 text-muted">Rigorous testing ensures that our solutions are robust, secure, and perform exactly as expected across all platforms and devices.</p>
                </div>
            </div>
            
            <!-- Step 5 -->
            <div class="row g-5 align-items-center mb-5 process-row">
                <div class="col-lg-6 wow slideInLeft" data-wow-delay="0.1s">
                    <div class="process-img-wrapper position-relative h-100">
                        <img class="img-fluid rounded shadow-lg float-anim" src="img/team-3.jpg" alt="Deployment" style="width: 100%; height: 400px; object-fit: cover;">
                        <div class="process-number-badge">5</div>
                    </div>
                </div>
                <div class="col-lg-6 wow slideInRight" data-wow-delay="0.3s">
                    <h2 class="mb-4">Deployment</h2>
                    <p class="mb-4 fs-5 text-muted">We seamlessly launch your project into the live environment with minimal disruption to your operations and maximum efficiency.</p>
                </div>
            </div>
            
            <!-- Step 6 -->
            <div class="row g-5 align-items-center mb-5 process-row flex-lg-row-reverse">
                <div class="col-lg-6 wow slideInRight" data-wow-delay="0.1s">
                    <div class="process-img-wrapper position-relative h-100">
                        <img class="img-fluid rounded shadow-lg float-anim-reverse" src="img/team-2.jpg" alt="Ongoing Support" style="width: 100%; height: 400px; object-fit: cover;">
                        <div class="process-number-badge left-badge">6</div>
                    </div>
                </div>
                <div class="col-lg-6 wow slideInLeft" data-wow-delay="0.3s">
                    <h2 class="mb-4">Ongoing Support</h2>
                    <p class="mb-4 fs-5 text-muted">Our team remains available to provide continuous support and maintenance as your business grows and scales up.</p>
                </div>
            </div>

        </div>
    </div>
    <!-- How It Works End -->"""

html_out = re.sub(r"<!-- How It Works Start -->.*?<!-- How It Works End -->", new_section, html, flags=re.DOTALL)
with codecs.open(html_path, 'w', 'utf-8') as f:
    f.write(html_out)

# 2. Update CSS
css_path = r"css\style.css"
css_addition = """
/* Grand Zigzag Process Styles */
.float-anim {
    animation: float 6s ease-in-out infinite;
}
.float-anim-reverse {
    animation: float-rev 6s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translateY(0px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    50% { transform: translateY(-20px); box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
    100% { transform: translateY(0px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
}
@keyframes float-rev {
    0% { transform: translateY(-20px); box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
    50% { transform: translateY(0px); box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    100% { transform: translateY(-20px); box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
}
.process-number-badge {
    position: absolute;
    top: -20px;
    right: -20px;
    width: 60px;
    height: 60px;
    background: var(--primary);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: bold;
    border-radius: 50%;
    border: 5px solid white;
    box-shadow: 0 10px 20px rgba(8, 163, 218, 0.4);
    z-index: 10;
}
.process-number-badge.left-badge {
    right: auto;
    left: -20px;
}
"""
with codecs.open(css_path, 'a', 'utf-8') as f:
    f.write(css_addition)
