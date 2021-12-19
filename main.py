from flask import Flask, request,render_template,Response
import json
from Training_Raw_data_validation.rawValidation import Raw_Data_validation
app=Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/train',methods=['POST'])
def trainRouteClient():
    try:
        folder_path = "Training_Batch_Files"
        if folder_path is not None:
            path = folder_path

            #train_valObj = train_validation(path)   #Object Initialization

            #train_valObj.train_validation()   #calling the training-validation function
    except ValueError:
        return Response("Error Occurred! %s"%ValueError)
    except KeyError:
        return Response("Error Occurred! %s"%KeyError)
    except Exception as e:
        return Response("Error Occurred! %s"%Exception)
    return Response("Training Successful!!")




if __name__=='__main__':
    app.run()