from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1= ChatGroq(model="llama-3.1-8b-instant")
model2= ChatGroq(model="llama-3.3-70b-versatile")

prompt1=PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)


prompt2=PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=['text']
)

prompt3=PromptTemplate(
    template="Merge the provided note and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
    
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        'notes': prompt1|model1|parser,
        'quiz' : prompt2|model2|parser
    }
)

merge_chain=prompt3|model1|parser

chain=parallel_chain | merge_chain

text= """
XGBoost, short for Extreme Gradient Boosting, is one of the most powerful and widely used machine learning algorithms for structured/tabular data. It is an implementation of the gradient boosting framework developed by Tianqi Chen and introduced in 2016. XGBoost has gained immense popularity in data science competitions (like Kaggle) and in industry applications due to its scalability, speed, and predictive power.

At its core, XGBoost is a decision-tree-based ensemble Machine Learning algorithm that uses a gradient boosting framework.

📚 What is Gradient Boosting?
Before diving into XGBoost, it's crucial to understand the concept of gradient boosting.

Gradient Boosting is an ensemble learning technique that builds a strong learner by combining multiple weak learners (usually decision trees) in a sequential manner. Each new tree attempts to correct the errors made by the previous ensemble of trees by minimizing a loss function using gradient descent.

The steps in gradient boosting:

Train a weak model (e.g., shallow decision tree) on the data.

Compute the residuals (errors).

Train the next model to predict these residuals.

Combine the predictions of all models.

This process is repeated iteratively, and at each step, the model learns from the mistakes of the previous one.

🚀 Why XGBoost?
XGBoost enhances the standard gradient boosting algorithm by incorporating several engineering optimizations and algorithmic improvements, making it faster and more accurate.

Key benefits of XGBoost:

Regularization (L1 and L2) to reduce overfitting.

Parallel processing (unlike traditional boosting algorithms).

Tree pruning for better performance.

Handling missing values automatically.

Built-in cross-validation.

Efficient memory usage.

Supports both regression and classification tasks.

🧠 How XGBoost Works
XGBoost builds trees sequentially like traditional boosting methods, but with improvements in speed and accuracy. Here’s a step-by-step explanation of its working:

1. Objective Function
XGBoost optimizes a custom objective function that consists of:

A loss function (e.g., log loss for classification, RMSE for regression).

A regularization term to penalize the complexity of the model.

2. Gradient Descent
Instead of minimizing loss directly, XGBoost uses second-order derivatives (gradient and hessian) to optimize the objective function efficiently. This makes convergence faster and more accurate.

3. Tree Construction
XGBoost uses a greedy algorithm to grow trees, choosing the best split based on the gain (improvement in the objective function). It supports depth-wise and loss-guided growth strategies.

4. Regularization
To avoid overfitting, XGBoost adds regularization to the loss function:

L1 regularization (Lasso): encourages sparsity.

L2 regularization (Ridge): penalizes large weights.

5. Shrinkage (Learning Rate)
After each boosting step, the contribution of each tree is scaled by a learning rate (also known as shrinkage). This helps prevent overfitting and improves generalization.

6. Column Subsampling
XGBoost can randomly sample features at each step (similar to Random Forest), which adds diversity and reduces overfitting.

🛠️ Hyperparameters of XGBoost
Here are some of the most important hyperparameters:

Hyperparameter	Description
n_estimators	Number of trees to be built.
max_depth	Maximum depth of a tree. Controls model complexity.
learning_rate	Step size shrinkage used in updates to prevent overfitting.
subsample	Percentage of rows used per tree (row sampling).
colsample_bytree	Percentage of features used per tree (feature sampling).
gamma	Minimum loss reduction required to make a split.
lambda	L2 regularization term on weights.
alpha	L1 regularization term on weights.
objective	Defines the loss function (e.g., 'reg:squarederror', 'binary:logistic').

🧪 Use Cases of XGBoost
XGBoost is widely used in many real-world applications, such as:

Kaggle Competitions – Often ranks among the top performing models.

Finance – Credit scoring, fraud detection.

Healthcare – Disease prediction, patient risk analysis.

Marketing – Customer churn prediction, customer segmentation.

Manufacturing – Defect detection, predictive maintenance.

📈 Model Evaluation
Common metrics used to evaluate XGBoost models include:

Classification: Accuracy, Precision, Recall, F1 Score, AUC-ROC.

Regression: Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), R² Score.
"""

result=chain.invoke({"text":text})

print(result)

chain.get_graph().draw_ascii()




