const T=window.TOOLS,F={job:"job",price:"price_tier",difficulty:"difficulty"},sel={};
const vals=k=>[...new Set(T.flatMap(t=>[].concat(t[F[k]])))].sort();
let h="";for(const k in F){h+=`<h4>${k.toUpperCase()}</h4>`+vals(k).map(v=>`<label><input type="checkbox" data-k="${k}" value="${v}"> ${v}</label>`).join("")}
document.getElementById("filters").innerHTML=h;
document.querySelectorAll("aside input,#q").forEach(i=>i.addEventListener("input",render));
function render(){const q=document.getElementById("q").value.toLowerCase();
 for(const k in F)sel[k]=[...document.querySelectorAll(`input[data-k=${k}]:checked`)].map(i=>i.value);
 const r=T.filter(t=>(!q||JSON.stringify([t.name,t.job,t.who]).toLowerCase().includes(q))
  &&Object.keys(F).every(k=>!sel[k].length||sel[k].includes(t[F[k]])));
 count.textContent=r.length+" tools";
 grid.innerHTML=r.map(t=>`<div class="card"><h3><a href="tool.html?id=${t.id}">${t.name}</a></h3><div><span class=tag>${t.job}</span><span class=tag>${t.difficulty} setup</span></div><p>${t.who}</p><p><b>${t.price_tier}</b> · ${t.starting_price}${t.pricing_verified?"":" <span class='tag warn'>unverified</span>"}</p></div>`).join("")}
render();
// Config: set these when the backends exist.
const SIGNUP_ENDPOINT="https://signup.kordaris.com"; // e.g. Resend audience endpoint; receives POST JSON {email}
const TALLY_FORM_URL=""; // e.g. https://tally.so/r/xxxx
const CONTACT="hello@kordaris.com";
if(TALLY_FORM_URL){const l=document.getElementById("suggest-link");l.href=TALLY_FORM_URL;l.target="_blank";l.rel="noopener"}
document.getElementById("nl-form").addEventListener("submit",async e=>{e.preventDefault();
 const em=document.getElementById("nl-email"),m=document.getElementById("nl-msg"),v=em.value.trim();
 if(!em.checkValidity()||!v){m.textContent="Please enter a valid email address.";em.focus();return}
 if(!SIGNUP_ENDPOINT){m.innerHTML=`Signups open soon — email <a href="mailto:${CONTACT}?subject=Newsletter%20signup&body=Please%20add%20me%3A%20${encodeURIComponent(v)}">${CONTACT}</a> and we'll add you.`;return}
 m.textContent="Subscribing…";
 try{const r=await fetch(SIGNUP_ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:v})});
  if(!r.ok)throw 0;m.textContent="Thanks! You're subscribed.";em.value=""}
 catch(_){m.innerHTML=`Something went wrong. Email <a href="mailto:${CONTACT}">${CONTACT}</a> to join.`}});
