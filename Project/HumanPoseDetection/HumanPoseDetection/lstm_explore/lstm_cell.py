import numpy as np

class LSTMCell:
    def __init__(self, input_dim, hidden_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        
        # Initialize weights and biases for input, forget, cell, and output gates
        self.W_i = np.random.randn(hidden_dim, input_dim + hidden_dim)
        self.b_i = np.zeros((hidden_dim, 1))
        
        self.W_f = np.random.randn(hidden_dim, input_dim + hidden_dim)
        self.b_f = np.zeros((hidden_dim, 1))
        
        self.W_c = np.random.randn(hidden_dim, input_dim + hidden_dim)
        self.b_c = np.zeros((hidden_dim, 1))
        
        self.W_o = np.random.randn(hidden_dim, input_dim + hidden_dim)
        self.b_o = np.zeros((hidden_dim, 1))
        
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def tanh(self, x):
        return np.tanh(x)
    
    def forward(self, x_t, h_prev, C_prev):
        # Concatenate input and previous hidden state
        concat = np.vstack((x_t, h_prev))
        
        # Input gate
        i_t = self.sigmoid(np.dot(self.W_i, concat) + self.b_i)
        
        # Forget gate
        f_t = self.sigmoid(np.dot(self.W_f, concat) + self.b_f)
        
        # Cell candidate
        C_tilde = self.tanh(np.dot(self.W_c, concat) + self.b_c)
        
        # Cell state
        C_t = f_t * C_prev + i_t * C_tilde
        
        # Output gate
        o_t = self.sigmoid(np.dot(self.W_o, concat) + self.b_o)
        
        # Hidden state
        h_t = o_t * self.tanh(C_t)
        
        return h_t, C_t

# Example usage
input_dim = 3  # Dimension of input vector
hidden_dim = 5  # Dimension of hidden state

lstm_cell = LSTMCell(input_dim, hidden_dim)

# Create a sequence of input vectors
sequence_length = 10
input_sequence = [np.random.randn(input_dim, 1) for _ in range(sequence_length)]

# Initialize previous hidden state and cell state
h_prev = np.zeros((hidden_dim, 1))
C_prev = np.zeros((hidden_dim, 1))

# Process the sequence through the LSTM cell
for t, x_t in enumerate(input_sequence):
    h_prev, C_prev = lstm_cell.forward(x_t, h_prev, C_prev)
    print(f"Time step {t+1}:")
    print("Input:", x_t.T)
    print("Hidden state:", h_prev.T)
    print("Cell state:", C_prev.T)
    print()