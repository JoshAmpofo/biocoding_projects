import streamlit as st
import keras
import numpy as np
from keras.preprocessing import image
import logging
from PIL import Image

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Poultry Disease Detector",
    page_icon="🐔",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2c3e50;
        font-size: 3rem !important;
        padding-bottom: 2rem;
    }
    .upload-section {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    try:
        model_path = 'D:/coding_projects/poultry_disease_detection/model_files/pdisease_detector.keras'
        model = keras.models.load_model(model_path)
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return None

# Main interface
def main():
    # Header
    st.title("🐔 Poultry Disease Detector")
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.write("""
        This application helps detect common poultry diseases using AI. 
        Simply upload a clear image of your poultry fecal matter for analysis.
        """)
        # Add a disclaimer
        st.warning("""
                   ⚠️ **IMPORTANT DISCLAIMER**
                
                This AI tool is for preliminary screening only and should not be used as a substitute for professional veterinary care.
                   
                - Results may not always be accurate
                - Always consult a certified veterinarian for proper diagnosis
                - Use this tool as a supplementary aid only
                - Regular veterinary check-ups are essential
                """)
        
        st.divider()
        st.markdown("### Detectable Conditions")
        st.write("- Coccidiosis Disease")
        st.write("- Newcastle Disease")
        st.write("- Healthy Status")

    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Upload Image")
        st.info("Remember: This tool provides preliminary analysis only. Always verify results with a veterinarian.", icon="ℹ️")
        uploaded_file = st.file_uploader(
            "Choose a poultry image...", 
            type=["jpg", "jpeg", "png"],
            help="Upload a clear image of the poultry matter for accurate detection"
        )

    # Process image and show results
    if uploaded_file is not None:
        model = load_model()
        
        if model is None:
            st.error("❌ Model not loaded. Please check the model path and try again.")
        else:
            try:
                # Display the uploaded image
                with col1:
                    image_display = Image.open(uploaded_file)
                    st.image(image_display, caption="Uploaded Image", use_container_width=True)

                # Process the image
                img = image.load_img(uploaded_file, target_size=(224, 224))
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array /= 255.0

                # Make prediction
                prediction = model.predict(img_array)
                predicted_class = np.argmax(prediction[0])
                confidence_score = float(np.max(prediction[0]))
                
                class_names = ['coccidiosis', 'healthy', 'newcastle']
                prediction_result = class_names[predicted_class]

                # Display results
                with col2:
                    st.markdown("### Analysis Results")
                    
                    # Status indicator
                    status_color = "green" if prediction_result == "healthy" else "red"
                    st.markdown(f"**Status:** <span style='color:{status_color}'>{prediction_result.title()}</span>", 
                              unsafe_allow_html=True)
                    
                    # Confidence score
                    st.progress(confidence_score)
                    st.markdown(f"**Confidence Score:** {confidence_score:.2%}")
                    
                    # Recommendations
                    st.markdown("### Recommendations")
                    if prediction_result == "healthy":
                        st.success("✅ Your poultry appears to be healthy! Continue with regular care.")
                    else:
                        st.warning(f"⚠️ Potential {prediction_result} disease detected!")
                        st.markdown("""
                        **Immediate Actions:**
                        1. Isolate affected birds
                        2. Contact a veterinarian
                        3. Monitor other birds for symptoms
                        """)

                logger.info(f"Prediction made: {prediction_result} with confidence {confidence_score:.2f}")

            except Exception as e:
                logger.error(f"Error processing image: {e}")
                st.error("❌ Error processing image. Please try again with a different image.")

if __name__ == "__main__":
    main()
