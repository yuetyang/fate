from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import regularizers

def nn_1():

    max_sequence_length = 9  # 请根据你的数据集调整最大序列长度
    out_dim = 50

    # 创建卷积神经网络模型
    model = Sequential()


    model.add(Embedding(input_dim=128, output_dim=out_dim, input_length=max_sequence_length))


    model.add(Conv1D(128, kernel_size=5, activation='relu'))


    model.add(GlobalMaxPooling1D())


    model.add(Dense(64, activation='relu'))


    model.add(Dense(5, activation='sigmoid'))

    # 编译模型
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])



    # 打印模型结构
    print(model.to_json())


def nn_2():

    model_nn = keras.Sequential()
    model_nn.add(layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(9,)))
    model_nn.add(layers.BatchNormalization())
    model_nn.add(layers.Dropout(0.5))

    model_nn.add(layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model_nn.add(layers.BatchNormalization())
    model_nn.add(layers.Dropout(0.5))

    model_nn.add(layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model_nn.add(layers.BatchNormalization())
    model_nn.add(layers.Dropout(0.5))


    model_nn.add(layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model_nn.add(layers.BatchNormalization())
    model_nn.add(layers.Dropout(0.5))

    model_nn.add(layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model_nn.add(layers.BatchNormalization())
    model_nn.add(layers.Dropout(0.5))

    print(model_nn.to_json()) 