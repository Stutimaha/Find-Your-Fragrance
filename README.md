# [Find Your Fragrance](https://find-your-fragrance.streamlit.app/)

## Introduction

I have created "[Find Your Fragrance](https://find-your-fragrance.streamlit.app/)" a website that assists you in discovering your perfect scent by leveraging the notes of your favorite perfume. With this website, you can effortlessly find your next signature fragrance. By utilizing machine learning algorithms, the website recommends five similar perfumes based on the perfume notes you provide, including the brand name, product name, and specific notes.

## Project Overview

The objective was to design a system that recommends five perfumes with notes similar to the user's most recent perfume search. To achieve this, I utilized Sentence-BERT to transform perfume notes into meaningful sentence embeddings. These embeddings were then compared using cosine similarity metrics to generate relevant perfume recommendations.

## Features

- User Input: You can enter the brand name, product name, and perfume notes to initiate the recommendation process.
- Similarity Analysis: The system transforms your provided perfume notes into semantically meaningful sentence embeddings using Sentence-BERT.
- Recommendation Engine: By employing cosine similarity metrics, the system generates a list of five perfumes with notes similar to your input.
- Personalized Experience: The recommender system ensures that the recommended perfumes align with your preferences, providing a personalized fragrance discovery journey.

## Usage
To experience "Find Your Fragrance" yourself, click [here](https://find-your-fragrance.streamlit.app/) and follow these simple steps:
1. Enter the brand name, product name, and perfume notes in the provided input fields.
2. Click the "Find Fragrance" button to initiate the recommendation process.
3. The system will analyze your input and generate a list of five similar perfumes.
4. Review the recommended perfumes and explore their details to find your next signature fragrance effortlessly.
