# cengizentel
[**@CengizEntel**](https://twitter.com/CengizEntel) is the Selenium based **Movie Recommendator Bot** who sends a good movie recommendaiton tweet per 3 hrs.

##### Update Notes:
* **v1.1** Some language fix
* **v1.0** Initial release

## To make your own bot with this project
You can make your movie recommendation bot 
#### 1 - Select **the Firefox Geckodriver** version suitable for your OS from [here](https://github.com/mozilla/geckodriver/releases) and add your project path. Then install the requirements:

```bash
pip install selenium
pip install pandas
pip install requests
pip install BeutifulSoup4
```
#### 2 - Edit these lines in *enviroment.py*
```python
def thePassword():
    return 'PUT YOUR EMAIL OR USERNAME HERE'

def theEmail():
    return 'PUT YOUR PASSWORD HERE'
```
#### 3 - Creating a CSV file as a recommendation database
Append movies to the *movies.csv* file by using ";" as delimeter.

#### 4 - Setting the tweet frequency
Edit the code at line 88 in *botmain.py*. Sleeping time (seconds) 10800 is for 3 hours. 
```python
while True:
    cengizentel.Tweetting()
    time.sleep(10800)
```
#### 5 - Run
Open a terminal in the project folder and run this code:
```bash
python botmain.py
```
Terminal outputs will be like this: 
```
The Bot is Online!
PUT YOUR EMAIL OR USERNAME HERE sent as email.
PUT YOUR PASSWORD HERE sent as password.
Nothing But the Truth || 2008 || IMDb: 7.2
Rod Lurie
Crime, Drama, Mystery
108min
#sinema #film #öneri #movie #cinema
https://www.imdb.com/title/tt1073241
2021-05-25 00:41:44.976390
**************
Harry Potter and the Deathly Hallows: Part 1 || 2010 || IMDb: 7.7
David Yates
Tür: Adventure, Family, Fantasy
146min
#sinema #film #öneri #movie #cinema
https://www.imdb.com/title/tt0926084
2021-05-25 03:41:44.976390
**************
```
## Notes
* Tweet char limit is 275.
* There is no try-except method; because I am not aware for now.
* I highly recommend to use venv.
* If you will install the bot on a remote server, You should use *enviroments.env* method for the secure your login info.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2021 Çağatay ÜRESİN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
