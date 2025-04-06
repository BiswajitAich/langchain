from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
"""

splitter=RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, chunk_size=300, chunk_overlap=0)
chunks = splitter.split_text(text=text)
print(chunks)
print("\n\n")
for i, item in enumerate(chunks):
    print(f"[{i+1}]->", item)
    print("\n")