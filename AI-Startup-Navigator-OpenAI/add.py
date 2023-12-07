from flask import Flask, render_template, request
import openai

app = Flask(__name__)


openai.api_key = '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'


@app.route('/')
def index():
    return render_template('index.html')  # 메인 페이지

@app.route('/submit_idea', methods=['POST'])
def submit_idea():
    idea = request.form['idea']
    if not idea.strip():
        error_message = "아이디어를 입력해주세요."
        return render_template('index.html', error=error_message)
    
    feedback = analyze_idea_with_openai(idea)
    return render_template('feedback.html', feedback=feedback)

@app.route('/generate-idea', methods=['GET', 'POST'])
def generate_idea():
    if request.method == 'POST':
        keywords = request.form['keywords']
        prompt = f"창업 아이디어 창출: 다음 키워드들을 활용하여 혁신적이고 실현 가능한 창업 아이디어를 제안해주세요. 키워드들이 아이디어의 핵심 요소로 적극적으로 통합되어야 합니다: {keywords}. 아이디어는 독창적이고 시장의 필요성을 충족시켜야 하며, 이 아이디어가 성공할 수 있는 이유와 잠재적인 고객층에 대해서도 설명해주세요."
        idea = openai_generate(prompt)
        return render_template('generate.html', idea=idea)
    return render_template('generate_idea.html')

@app.route('/solve-problem', methods=['GET', 'POST'])
def solve_problem():
    if request.method == 'POST':
        problem = request.form['problem']
        prompt = f"비즈니스 문제 분석 및 해결 제안: '{problem}'에 대해 상세한 분석을 수행하고, 이 문제를 해결할 수 있는 구체적이고 실용적인 전략을 제시해주세요. 해결책은 창의적이면서도 실행 가능해야 하며, 해당 문제의 근본적인 원인과 해결 방안에 대해 명확하게 설명해야 합니다."
        solution = openai_generate(prompt)
        return render_template('solution.html', solution=solution)
    return render_template('solve_problem.html')

@app.route('/create-marketing-content', methods=['GET', 'POST'])
def create_marketing_content():
    if request.method == 'POST':
        description = request.form['description']
        prompt = f"마케팅 콘텐츠 개발: '{description}'에 대한 매력적이고 설득력 있는 마케팅 콘텐츠를 작성해주세요. 이 콘텐츠는 제품/서비스의 주요 특징과 혜택을 강조하며, 타겟 고객층에게 어떻게 가치를 제공할 수 있는지를 명확하게 전달해야 합니다. 또한, 창의적이고 독창적인 방식으로 고객의 관심을 끌 수 있도록 해주세요."
        marketing_content = openai_generate(prompt)
        return render_template('marketing_content.html', content=marketing_content)
    return render_template('create_marketing_content.html')

@app.route('/market-analysis', methods=['GET', 'POST'])
def market_analysis():
    if request.method == 'POST':
        market_query = request.form['market_query']
        prompt = f"상세 시장 분석 요청: '{market_query}'에 대해 깊이 있는 시장 분석을 수행해주세요. 이 분석은 시장의 현재 동향, 주요 경쟁자, 잠재적 기회 및 위험 요소, 타겟 고객층의 특성, 그리고 예상되는 산업 변화 등을 포함해야 합니다. 또한, 이 시장에서 성공하기 위한 전략적 제안도 포함시켜 주세요."
        analysis = openai_generate(prompt)
        return render_template('market.html', analysis=analysis)
    return render_template('market_analysis.html')

def openai_generate(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000
    )
    return response.choices[0].text.strip()


def analyze_idea_with_openai(idea):
    openai.api_key = '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'

    response = openai.Completion.create(
      engine="text-davinci-003",
 prompt = (
    f"다음은 창업 계획에 대한 상세한 분석 요청입니다: '{idea}'. "
    "이 비즈니스의 잠재적 시장 규모, 타겟 고객, 위치, 산업의 경쟁 구도에 대해 분석해주세요. "
    "가격 정책, 마케팅 전략, 재정 관리 방법에 대한 제안을 포함해주세요. "
    "또한, 이 비즈니스 모델이 직면할 수 있는 주요 위험 요소와 이를 관리하기 위한 전략, 그리고 성공적인 창업을 위해 필요한 주요 단계들에 대해서도 설명해주세요."
)
,
       max_tokens=3000
    )

    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
    



