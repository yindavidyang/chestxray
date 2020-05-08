protoc --decode onnx.ModelProto onnx.proto < pneumonia.onnx > pneumonia.onnx.txt
protoc --encode onnx.ModelProto onnx.proto < pneumonia2.onnx.txt > pneumonia2.onnx
