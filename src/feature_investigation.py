import matplotlib.pyplot as plt

def signal_processing_histogram(df, feature, feature_title):
    signal = df[df["Label"] == "s"]
    noise = df[df["Label"] == "b"]
    plt.hist(signal[feature], alpha = 0.5, label = "Signal")
    plt.hist(noise[feature], alpha = 0.5, label = "Noise")
    plt.title(f"Impact of {feature_title}")
    plt.xlabel(feature)
    plt.ylabel("Event Count")
    plt.legend()
    return plt.show()