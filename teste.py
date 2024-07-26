import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Exemplo de DataFrame filtrado (substitua pelo seu DataFrame real)
data = {
    'data': pd.date_range(start='1/1/2020', periods=100, freq='M'),
    'ferro': [0.05 + (x/200) for x in range(100)],
    'local': ['Ponto1']*50 + ['Ponto2']*50
}
filtered_df = pd.DataFrame(data)

# Criação do gráfico de Ferro usando Plotly Express
fig = px.line(filtered_df, x='data', y='ferro', title='Valores de Ferro', color='local', template="simple_white",
              labels={'data': 'Anos',
                      'ferro': 'Ferro',
                      'local': 'Pontos'})

# Convertendo para go.Figure para adicionar a linha horizontal
fig = go.Figure(fig)

# Adicionando a linha horizontal
fig.add_shape(
    type="line",
    x0=filtered_df['data'].min(), x1=filtered_df['data'].max(),
    y0=0.100, y1=0.100,
    line=dict(color="Red", width=2, dash="dash"),
)

# Colunas no Streamlit
c1, c2, c3 = st.columns((3, 0.5, 3))

# Conteúdo da coluna 1
c1.header('Ferro')
c1.plotly_chart(fig, theme='streamlit', use_column_width=True)

# Conteúdo da coluna 3
# Supondo que o gráfico de manganês (p_mang) já esteja definido
p_mang = go.Figure()  # substitua por seu gráfico real de manganês
c3.header('Manganês')
c3.plotly_chart(p_mang, theme='streamlit', use_column_width=True)

#FATAL ERROR?
#POSSÍVEIS ERROS
#INSERÇÃO DE CARACTER ESPECIAL - no
#STREAMLIT - REINSTALAR 