import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.title("이미지 색상 추출기")
st.write("이미지를 업로드하면 주요 색상 5가지를 추출하여 시각화 합니다.")

uploaded_file = st.file_uploader("이미지를 업로드 해주세요. (jpg, png)", type=["jpg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption = "업로드된 이미지")
    data = np.array(image).reshape(-1, 3)
    kmeans = KMeans(n_clusters=5, random_state=42)
    kmeans.fit(data)

    colors = kmeans.cluster_centers_.astype(int)

    fig, ax = plt.subplots(figsize=(8, 2))

    for i, color in enumerate(colors):
        ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color/255))
    
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.axis('off')
    st.pyplot(fig)

    st.subheader("추출된 색상 코드")

    for i, color in enumerate(colors):
        rgb = tuple(color)
        hex_code = '#%02x%02x%02x' % rgb
        st.write(f"{i+1}, RGB:{rgb}, HEX:{hex_code}")