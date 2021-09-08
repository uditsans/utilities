<h1>Web Scrapping</h1>

<p>There are two types of web-scrapping methods:</p>
<ol>
    <li>
        <strong>Static web-scrapping</strong>
        <p>
            We can use static web-scrapping method for those use-cases where there are no dynamic elements (such as, Javascripts and Forms).
        </p>
    </li>
    <li>
    <strong>Dynamic web-scrapping</strong>
        <p>
            We can use dyanamic web-scrapping method for those use-cases when dealing with scripts and cases where login is required.
        </p>
    </li>
</ol>
<h3>Tools for static web-scrapping</h3>
<p>For doing static web-scrapping through python, one needs to install the following libraries:</p>
<ul>
    <li><p><strong>HTML Selector:</strong> The library is able to parse HTML and CSS tags. Few of the commonly used HTML selectors are:</p>
    <ol>
    <li><strong>Parsel: </strong><code>pip install parsel</code></li>
    <li><strong>BeautifulSoup4: </strong><code>pip install beautifulsoup4</code></li>
    </ol></li><br>
    <li><p><strong>Python Parser:</strong> The library is used to enable the HTML selector to parse the HTML and CSS tags. Few of the commonly used parsers are:</p>
    <ol>
    <li><strong>lxml parser: </strong><code>pip install lxml</code></li>
    <li><strong>html5lib parser: </strong><code>pip install html5lib</code></li>
    </ol></li>    
</ul>

<h3>Tools for dynamic web-scrapping</h3>
<p>For doing dynamic web-scrapping through python, one needs to install the following libraries:</p>
<ul>
    <li><p><strong>Selenium:</strong> Selenium is an automation tool that enables adding login credentials and doing dynamic clicks. To use Selenium one needs through Python one needs to install it using <code>pip install selenium</code> Additionally, we would also need to install webdrivers. The link for them are:</p>
    <ol>
        <li><a href='https://github.com/mozilla/geckodriver/releases'><strong>GeckoDriver</strong></a> for Firefox. <em>Kindly install the latest driver.</em></li>
        <li><a href='https://chromedriver.chromium.org/downloads'><strong>ChromeDriver</strong></a> for Google Chrome. <em>Kindly install the driver version compatible with the Chrome version on your system .</em></li>
        <li><a href='https://github.com/operasoftware/operachromiumdriver/releases'><strong>OperaDriver</strong></a> for Opera. <em>Kindly install the latest driver.</em></li>
        </ol></li>
</ul>

