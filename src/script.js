const form = document.querySelector("#legendform")
const alias = document.querySelector('#alias');
const quote = document.querySelector('#quote');
const wiki = document.querySelector('#wiki');
const realname = document.querySelector('#realname');
const age = document.querySelector('#age');
const homeworld = document.querySelector('#homeworld');
const class_ = document.querySelector('#class_');
const classpassive = document.querySelector('#classpassive');
const tactical = document.querySelector('#tactical');
const tacticalwiki = document.querySelector('#tacticalwiki');
const passive = document.querySelector('#passive');
const passivewiki = document.querySelector('#passivewiki');
const ultimate = document.querySelector('#ultimate');
const ultimatewiki = document.querySelector('#ultimatewiki');
const addButton = document.querySelector('button[type="submit"]');
const addedData = document.querySelector('#addedData')
form.addEventListener("submit", (e) => {
  e.preventDefault();
  let legendData = {};
  legendData.alias = alias.value;
  legendData.quote = quote.value;
  legendData.wiki = wiki.value;
  legendData.realname = realname.value;
  legendData.age = age.value;
  legendData.homeworld = homeworld.value;
  legendData.class_ = class_.value;
  legendData.classpassive = classpassive.value;
  legendData.tactical = tactical.value;
  legendData.tacticalwiki = tacticalwiki.value;
  legendData.passive = passive.value;
  legendData.passivewiki = passivewiki.value;
  legendData.ultimate = ultimate.value;
  legendData.ultimatewiki = ultimatewiki.value;
  sendToDB(legendData)
})

async function sendToDB(data) {
  const url = "http://localhost:8000/addLegend";
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      // Handle non-successful response
      const errorData = await response.json();
      console.error('Error:', errorData);
    } else {
      // Successful response
      const result = await response.json();
      addedData.innerHTML = result
      console.log(result);
    }
  } catch (error) {
    // Handle any unexpected errors
    console.error('An unexpected error occurred:', error);
  }
}

