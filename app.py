from quart import Quart, render_template, jsonify, request, send_file
from chatbot.chains import chatbot_reply_chain

app = Quart(__name__)


level_two_summary = """
Hey Pumpkin Porters team! We wanted to create this quick audio summary to walk you through the key findings from our latest marketing report.

First, fantastic news on Instagram! Impressions jumped by over 500 percent in August, showing real momentum in our local brand visibility. Facebook posts and ad clicks also saw big increases, and we’re maintaining a perfect review response rate—great job building trust with our audience.

However, we do have some challenges to address. Facebook ad performance dropped in August, with fewer clicks and higher costs. This means it’s time to refresh our ad creatives to get those numbers back up. Also, Google Ads weren’t active last month, so we missed out on potential new customers there.

Looking ahead, our top priorities are: submitting new, seasonal content for Instagram to keep that growth going; relaunching Google Ads to drive at least 150 clicks; and updating Facebook ad visuals and copy to boost engagement. Let’s also keep sharing customer stories and reviews to connect with our community.

In summary, we’re making strong progress, especially on Instagram, but we need to act quickly on ad updates and Google campaigns to keep the momentum. Thanks for your hard work, and let’s keep pushing for even better results this month!
"""

# Sample takeaways data in markdown format
SAMPLE_TAKEAWAYS = """
• **Instagram impressions surged by 548%** - from 60 in July to 389 in August, showing explosive social media growth

• **Facebook Ads delivered 469 clicks at 12.14% CTR in July** - with efficient $0.31 CPC in August, though creative refresh needed

• **100% review response rate maintained** - building crucial trust and credibility with local customer base

• **Facebook posts doubled from 5 to 11** - representing 548% growth in content output and brand visibility

• **Google Ads represent untapped opportunity** - currently inactive but could generate 150+ clicks when relaunched

• **September action plan focuses on creative refresh** - new ad visuals needed to restore 12%+ CTR performance

• **Social media follower targets on track** - Facebook approaching 30-50 range, Instagram progressing toward 18-30 goal

• **Seasonal content strategy ready for implementation** - fall events and customer stories to drive 1,000+ impressions per platform
"""
SAMPLE_TRANSCRIPT = level_two_summary


@app.route("/")
async def index():
    return await render_template("index.html")


@app.route("/api/transcript")
async def get_transcript():
    return jsonify({"transcript": SAMPLE_TRANSCRIPT, "takeaways": SAMPLE_TAKEAWAYS})


@app.route("/api/chat", methods=["POST"])
async def chat():
    data = await request.get_json()
    query = data.get("query", "")
    response = await chatbot_reply_chain(query=query, chat_history=[])

    return jsonify({"response": response})


@app.route("/audio/<filename>")
async def serve_audio(filename):
    return await send_file(f"audio/{filename}")


@app.route("/video/<filename>")
async def serve_video(filename):
    return await send_file(f"video/{filename}")


@app.route("/pdf/<filename>")
async def serve_pdf(filename):
    return await send_file(f"pdf/{filename}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
