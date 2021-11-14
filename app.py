from fastapi import FastAPI 
from pydantic import BaseModel 
import uvicorn
app = FastAPI()
from sklearn.linear_model import LogisticRegression 
import pandas as pd 
import pickle #we are loading the model using pickle 
import regression_model
from regression_model import predict
import numpy as np
class House(BaseModel): 
	Id: int
	MSSubClass: int
	MSZoning: str
	LotFrontage: float
	LotArea: int
	Street: str
	Alley: str
	LotShape: str
	LandContour: str
	Utilities: str
	LotConfig: str
	LandSlope: str
	Neighborhood: str
	Condition1: str
	Condition2: str
	BldgType: str
	HouseStyle: str
	OverallQual: int
	OverallCond: int
	YearBuilt: int
	YearRemodAdd: int
	RoofStyle: str
	RoofMatl: str
	Exterior1st: str
	Exterior2nd: str
	MasVnrType: str
	MasVnrArea: float
	ExterQual: str
	ExterCond: str
	Foundation: str
	BsmtQual: str
	BsmtCond: str
	BsmtExposure: str
	BsmtFinType1: str
	BsmtFinSF1: float
	BsmtFinType2: str
	BsmtFinSF2: float
	BsmtUnfSF: float
	TotalBsmtSF: float
	Heating: str
	HeatingQC: str
	CentralAir: str
	Electrical: str
	FirstFlrSF: int
	SecondFlrSF: int
	LowQualFinSF: int
	GrLivArea: int
	BsmtFullBath: float
	BsmtHalfBath: float
	FullBath: int
	HalfBath: int
	BedroomAbvGr: int
	KitchenAbvGr: int
	KitchenQual: str
	TotRmsAbvGrd: int
	Functional: str
	Fireplaces: int
	FireplaceQu: str
	GarageType: str
	GarageYrBlt: float
	GarageFinish: str
	GarageCars: float
	GarageArea: float
	GarageQual: str
	GarageCond: str
	PavedDrive: str
	WoodDeckSF: int
	OpenPorchSF: int
	EnclosedPorch: int
	ThreeSsnPortch: int
	ScreenPorch: int
	PoolArea: int
	PoolQC: str
	Fence: str
	MiscFeature: str
	MiscVal: int
	MoSold: int
	YrSold: int
	SaleType: str
	SaleCondition: str
@app.get("/") 
def home():
	print("hhhhhhhhhhhhhhhhhhhh")
	return {'ML model for test prediction'} 
@app.post('/make_predictions')
async def make_predictions(house:House):
    house_dict=house.__dict__
    house_df = pd.DataFrame(house_dict, index=[0])
    house_df=house_df.replace('nan',np.nan)
    return(regression_model.predict.make_prediction(input_data=house_df))
if __name__ == "__main__": 
	uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)