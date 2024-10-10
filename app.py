from flask import Flask, render_template, request

app = Flask(__name__)

# Sample responses for rice mill SEO-related questions
responses = {
    "hi": "Hello! How can I assist you with your rice milling questions today?",
    "how are you?": "I'm just a program, but I'm doing great! How about you?",
    "what's your name?": "I'm a simple chatbot created with Flask. What's your name?",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "bye": "Goodbye! Have a great day!",
    "what's up": "How can I help you today?",
    
    # Rice Mill SEO-related questions and answers
    "what is rice milling?": "Rice milling is the process of removing the husk and bran layers from paddy to produce edible white rice.",
    "how does a rice mill work?": "A rice mill works by using a series of machines to remove the outer husk, bran, and germ layers, leaving the starchy endosperm.",
    "what are the types of rice mills?": "There are two main types: small-scale and large-scale rice mills. Small-scale mills are used by farmers, while large-scale mills are for industrial purposes.",
    "how can i improve my rice mill seo?": "To improve your rice mill SEO, focus on local keywords, optimize your website with content like 'rice milling process,' and list your business on local directories.",
    "what keywords should i use for rice mill seo?": "Use keywords like 'rice milling services,' 'bulk rice suppliers,' 'organic rice mill,' and local terms such as 'rice mill in [Your Location].'",
    "what is the best rice mill for small businesses?": "The best rice mill for small businesses depends on production needs, but compact models from Satake or Bühler are often recommended.",
    "what is the process of rice milling?": "The rice milling process involves cleaning, hulling, milling, and polishing to produce high-quality rice.",
    "how can i market my rice mill online?": "You can market your rice mill by creating a website, using social media platforms, optimizing your site for SEO, and listing on agricultural directories.",
    "what are the benefits of modern rice milling machines?": "Modern rice milling machines improve efficiency, produce higher-quality rice, and reduce wastage compared to traditional methods.",
    "how do i reduce rice milling costs?": "You can reduce costs by optimizing operations, using energy-efficient machines, and investing in quality milling equipment that minimizes waste.",
    "what are the challenges in the rice milling industry?": "Common challenges include fluctuating raw material prices, high operational costs, and maintaining the quality of rice during milling.",
    "how can i increase production in my rice mill?": "You can increase production by upgrading to modern milling machines, improving workforce training, and optimizing production workflows.",
    "how can i export rice from my rice mill?": "To export rice, you need to comply with export regulations, obtain certifications, and establish relationships with international buyers.",
    "what is the shelf life of milled rice?": "Milled rice typically has a shelf life of 6-12 months if stored properly in cool, dry conditions.",
    "how do i choose the right rice mill equipment?": "Choose equipment based on production capacity, efficiency, and your budget. Popular brands like Satake and Bühler offer high-quality options.",
    "what are the main products of a rice mill?": "The main products are white rice, brown rice, rice bran, and rice husk, which can be used for various industrial purposes.",
    "what is the difference between brown rice and white rice?": "Brown rice is whole grain rice that retains its bran and germ, making it more nutritious, while white rice has been milled to remove these layers.",
    "how to store milled rice properly?": "Store milled rice in a cool, dry place, preferably in airtight containers to keep moisture and pests away.",
    "what are the uses of rice husk?": "Rice husk can be used as a fuel source, in building materials, or as a soil amendment in agriculture.",
    "how can technology improve rice milling?": "Technology can enhance efficiency through automation, improve quality control, and optimize energy usage.",
    "what are the environmental impacts of rice milling?": "The environmental impacts include waste generation, energy consumption, and air emissions. Sustainable practices can help mitigate these effects.",
    "how do I choose the right location for a rice mill?": "Choose a location close to rice-producing areas, with good transportation access and availability of labor and utilities.",
    "what are the maintenance requirements for rice milling machines?": "Regular cleaning, lubrication, and inspection of components are essential for maintaining milling machines.",
    "how can I find suppliers for rice mill machinery?": "You can find suppliers through online directories, trade shows, and industry associations.",
    "what is the role of rice bran in nutrition?": "Rice bran is rich in dietary fiber, vitamins, and healthy fats, making it a nutritious addition to diets and animal feed.",
    "how do I conduct market research for my rice mill?": "Conduct surveys, analyze industry trends, and study competitors to understand market demand and opportunities.",
    "what are the safety measures in a rice mill?": "Implement safety measures such as proper equipment maintenance, training for workers, and adherence to safety regulations.",
    "how to increase the shelf life of milled rice?": "Proper storage in airtight containers at low temperatures can help increase the shelf life of milled rice.",
    "what is the process of parboiling rice?": "Parboiling rice involves soaking, steaming, and drying paddy before milling, which helps retain nutrients and improve texture.",
    "what are the common challenges in rice milling?": "Common challenges include machinery breakdown, fluctuating prices of raw materials, and maintaining consistent quality.",
    "how can I differentiate my rice mill from competitors?": "Differentiate your mill by focusing on quality, unique product offerings, superior customer service, and effective branding.",
    "what types of rice can be milled?": "Common types of rice include long-grain, short-grain, basmati, jasmine, and sticky rice.",
    "what is the average yield of a rice mill?": "The average yield depends on the type of rice and milling efficiency, typically ranging from 60-75% of the paddy weight.",
    "how to deal with rice pests?": "Implement pest management strategies such as proper storage, regular inspections, and using natural repellents.",
    "what certifications are needed for a rice mill?": "Certifications may include food safety certifications (like HACCP), organic certifications, and local regulatory approvals.",
    "how can I increase customer satisfaction in my rice mill?": "Increase satisfaction by providing high-quality products, timely deliveries, and excellent customer service.",
    "what is the impact of climate change on rice production?": "Climate change can affect rice yield due to changes in rainfall patterns, temperature, and increased pests and diseases.",
    "what financing options are available for starting a rice mill?": "Financing options include bank loans, government grants, and investments from private equity or venture capital.",
    "how do I develop a business plan for my rice mill?": "A business plan should include market analysis, operational plans, financial projections, and strategies for growth.",
    "what are the most common rice mill machinery brands?": "Popular brands include Satake, Bühler, and Lushan, known for their quality and efficiency.",
    "how do I train staff for operating rice milling machines?": "Provide hands-on training, safety protocols, and regular workshops to ensure staff are well-equipped to operate machinery safely.",
    "what is the cost of setting up a rice mill?": "The cost can vary significantly based on location, scale, and equipment, but it typically ranges from a few thousand to several million dollars.",
    "how can I leverage social media for my rice mill?": "Use social media to showcase products, share customer testimonials, and engage with the community to build brand awareness.",
    "what are the different grades of rice?": "Rice is graded based on size, quality, and color, with common grades including premium, grade A, and grade B.",
    "how does rice milling affect nutritional value?": "Milling removes some nutrients, particularly in the bran and germ, but processes like parboiling can help retain more nutrients.",
    "how do I market organic rice from my mill?": "Emphasize the health benefits, sustainability, and certifications of your organic rice in your marketing materials and outreach.",
    "what is the role of rice in global food security?": "Rice is a staple food for over half of the world's population, playing a critical role in food security and nutrition.",
    "how do I analyze the profitability of my rice mill?": "Analyze costs, revenues, and market demand to determine profit margins and identify areas for improvement.",
    "what are the export regulations for rice?": "Export regulations vary by country but typically include quality standards, certifications, and labeling requirements.",
    "how can I improve the efficiency of my rice milling process?": "You can improve efficiency by streamlining workflows, investing in modern equipment, and training staff effectively.",
    "what innovations are changing the rice milling industry?": "Innovations include automation, AI for quality control, and sustainable practices that reduce waste and energy consumption.",
    "how do I handle rice quality complaints?": "Address complaints promptly, investigate the issue, and communicate transparently with customers to maintain trust.",
    "what are the economic impacts of rice milling on local communities?": "Rice milling can create jobs, stimulate local economies, and support agricultural development in rural areas.",
    "how to create a website for my rice mill?": "Use website builders or hire a developer to create a site showcasing your products, services, and contact information.",
    "what is the significance of rice in cultural traditions?": "Rice is often associated with prosperity and fertility in many cultures, playing a central role in rituals and celebrations.",
    "how can I build partnerships with local farmers?": "Build partnerships through outreach, offering fair prices, and providing support services like storage or transportation.",
    "what are the health benefits of consuming rice?": "Rice is a source of energy, providing carbohydrates, and is gluten-free, making it suitable for those with gluten intolerance.",
    "how do I create a sustainable rice milling operation?": "Implement practices that minimize waste, conserve energy, and support local agriculture to create a sustainable operation.",
    "what are the trends in rice consumption globally?": "Trends include increasing demand for organic and specialty rice varieties, driven by health-conscious consumers.",
    "how can I use data analytics in my rice mill?": "Data analytics can help optimize operations, track inventory, and analyze market trends for better decision-making.",
    "what is the future of rice milling technology?": "The future includes advancements in automation, AI, and sustainability, making milling more efficient and environmentally friendly.",
    "how do I ensure food safety in my rice mill?": "Implement food safety standards, conduct regular inspections, and provide staff training on hygiene and safety practices.",
    "what are the benefits of diversifying rice mill products?": "Diversifying can increase revenue streams, reduce risk, and cater to different market segments."
}

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", messages=[])

@app.route("/send", methods=["POST"])
def send():
    user_message = request.form["message"]
    response = responses.get(user_message.lower(), "I'm sorry, I don't understand that.")
    
    messages = [f"You: {user_message}", f"Bot: {response}"]
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
