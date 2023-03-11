import streamlit as st
import pandas as pd
import pickle
from sentence_transformers import util

# Load the model and data from the pickle file
with open('FYF_model.pkl', 'rb') as f:
    model_dict = pickle.load(f)

model = model_dict['model']
df = model_dict['df']
note_embeddings = model_dict['note_embeddings']


# Define a function to get perfume recommendations based on user input
def get_recommendation(user_perfume, user_notes):
    # Encode user notes
    user_embeddings = model.encode([user_notes], show_progress_bar=True)

    # Calculate cosine similarity scores between user embeddings and dataset embeddings
    cosine_scores = util.cos_sim(user_embeddings, note_embeddings)

    # Create dataframe to store cosine similarity scores for each perfume
    recommendations = pd.DataFrame({'Perfume': df['Name'], 'Score': cosine_scores[0]})

    # Sort recommendations by score
    recommendations = recommendations.sort_values(by='Score', ascending=False)

    # Remove the user's perfume from the recommendations
    recommendations = recommendations[recommendations['Perfume'] != user_perfume]

    # Sort the scores in descending order and recommend top 5 perfumes
    my_pairs=[]
    for j in range(cosine_scores.shape[1]):
        my_pairs.append({"index": j, "score": cosine_scores[0][j]})
    my_sorted_pairs = sorted(my_pairs, key=lambda x: x['score'], reverse=True)

    # Display the top 5 recommendations
    st.subheader(f"Top 5 Recommendations for {user_perfume}:")
    for no, pair in enumerate(my_sorted_pairs[:5]):
        st.write(f" {no+1}. {df.iloc[pair['index'], 0]} (Score: {pair['score']:.2f})")



    

# Define the Streamlit app
def main():
    # Set the page title and icon
    st.set_page_config(page_title='Find Your Fragrance', page_icon='https://png.pngtree.com/png-clipart/20210815/original/pngtree-watercolor-perfume-blue-glass-bottle-perfume-png-image_6644129.jpg')
    
    
    # Set the background image
    page_bg_img = '''
    <style>
        [data-testid="stAppViewContainer"]
            {
                background-image: url("https://media.glamourmagazine.co.uk/photos/613892f3e2e190b1f7b26136/16:9/w_2560%2Cc_limit/gettyimages-959786750_sf.jpg");
                background-size: cover;        
            }
        [data-testid="stHeader"]
            {
                background-color: rgba(0,0,0,0);
            }
        [data-testid="stVerticalBlock"]
            {
                background-color: #742a40;
            }
        .st-bt 
            {
            background-color: #DE5D83;
            }    
        .css-5uatcg 
        {
            background-color: #DE5D83;
            display: block;
            margin: 0 auto;
            text-align: center;
            border-radius: 100 px;   
        }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    


    # Set the app title and subtitle
    
    st.header("Find your Fragrance")
    st.subheader("Find your next signature perfume!")

    
    # Create a text box to enter the perfume Brand and Name
    selected_perfume = st.text_input('Enter the perfume name: (Brand name - Perfume Name)', placeholder='Jo Malone - English Pear & Freesia' )

    # Create a text box to enter the perfume notes
    notes = st.text_input('Enter the perfume notes: (comma separated)', placeholder= 'Pear, Melon, Freesia, Rose, Musk, Patchouli, Rhuburb, Amber')

    # Create a button to get recommendations
    if st.button('Get Recommendations'):
        if not selected_perfume and not notes:
            st.warning('Please enter the perfume name and notes.')
        elif not selected_perfume:
            st.warning('Please enter the perfume name.')
        elif not notes:
            st.warning('Please enter the perfume notes.')
        elif not all(x.strip() for x in notes.split(',')):
            st.warning('Please enter at least one note.')
        else:
            # Call the recommendation function and display the results
            get_recommendation(selected_perfume, notes)
            
            
if __name__ == '__main__':
    main()
