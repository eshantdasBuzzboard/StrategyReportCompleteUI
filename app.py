from quart import Quart, render_template, jsonify, request, send_file
from chatbot.chains import chatbot_reply_chain

app = Quart(__name__)

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
SAMPLE_TRANSCRIPT = """
Executive Summary:
This Strategic Kit Report provides comprehensive insights into Pumpkin Porters' social performance metrics for August 2024. Our analysis reveals significant growth opportunities in community engagement and sustainability initiatives.

Key Performance Indicators:
- Community Engagement Score: 87% (↑12% from July)
- Sustainability Index: 78% (↑8% from July)
- Brand Sentiment: Positive 89% (↑15% from July)

Strategic Recommendations:
1. Expand community outreach programs in Q4
2. Implement enhanced sustainability tracking systems
3. Leverage positive brand sentiment for customer acquisition

Market Analysis:
The craft beverage industry continues to show strong growth potential, with consumer preferences shifting towards locally-sourced and environmentally conscious brands. Pumpkin Porters is well-positioned to capitalize on these trends.

Financial Performance:
Revenue growth of 23% year-over-year demonstrates the effectiveness of current strategic initiatives. Cost optimization opportunities identified in supply chain management.

Risk Assessment:
Low to moderate risk profile with primary concerns around seasonal demand fluctuations and supply chain dependencies.

Next Steps:
1. Schedule quarterly review meeting
2. Implement recommended strategic initiatives
3. Monitor KPI progress monthly
"""


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
