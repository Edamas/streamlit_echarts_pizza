import streamlit as st
from streamlit_echarts import st_echarts

# Configura o layout do Streamlit para wide
st.set_page_config(layout="wide")

def render_pie_chart():
    options = {
        "title": {
            "text": "Áreas de Responsabilidade no Projeto Integrador",
            "subtext": "",
            "left": "center",
            "textStyle": {"fontSize": 20, "fontWeight": "bold"},
        },
        "tooltip": {
            "trigger": "item", 
            "formatter": "{a} <br/>{b} : {c} ({d}%)"
        },
        "legend": {
            "orient": "horizontal",
            "bottom": "0%",
            "left": "center",
            "itemWidth": 16,
            "itemHeight": 16,
            "textStyle": {"fontSize": 12},
        },
        "series": [
            {
                "name": "Responsabilidades",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": True,
                "itemStyle": {  
                    "borderRadius": 10,
                    "borderColor": "#fff",
                    "borderWidth": 0.5,
                },
                "label": {
                    "show": True,
                    "position": "outside",
                    "formatter": "{b} \n{c} ({d}%)",
                    "fontSize": 14,
                    "textBorderColor": "transparent",  # Remove a borda do texto
                    "textBorderWidth": 0  # Remove a borda do texto
                },
                "labelLine": {"show": True, "length": 10, "length2": 10},
                "data": [
                    {"value": 20, "name": "Desenvolvimento Backend"},
                    {"value": 15, "name": "Desenvolvimento Frontend"},
                    {"value": 15, "name": "Análise de Dados (Backend)"},
                    {"value": 10, "name": "Infraestrutura de TI (server, storage)"},
                    {"value": 10, "name": "Gestão de Projetos"},
                    {"value": 15, "name": "Documentação"},
                    {"value": 10, "name": "Vídeo de Apresentação"},
                    {"value": 10, "name": "Reuniões com o Grupo"},
                    {"value": 5, "name": "Testes e Validação"},
                    {"value": 5, "name": "Reuniões com o Orientador"},
                    {"value": 5, "name": "Pesquisa com Usuários"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }

    st_echarts(
        options=options, height="800px"
    )

if __name__ == "__main__":
    render_pie_chart()
