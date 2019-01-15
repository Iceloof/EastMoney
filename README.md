# Reuters
Retrieve A-share information from EastMoney for Python

## Install
```
pip install EastMoney
```

## Usage
- Initializing
```
from EastMoney import EastMoney
em=EastMoney('600320','SH')#EastMoney('300015','SZ')
```
- Get full info
It will return `{'code':'...','price':'...','PE':'...','marketCap':'...','company':'...','company_name_en':'...','company_name_cn':'...','industry':'...','area':'...','desc':'...'}`
```
em.getInfo()
```
- Get code
```
em.getCode()
```
- Get current price
```
em.getPrice()
```
- Get name
```
em.getName()
```
- Get company full name
```
em.getCompanyName()
```
- Get company full name in English
```
em.getCompanyName(lang='EN')
```
- Get market capital
```
em.getMarketCap()
```
- Get PE
```
em.getPE()
```
- Get company industry
```
reuters.getIndustry()
```
- Get company location
```
reuters.getLoc()
```
- Get company full description
```
reuters.getDesc()
```
