/* Generic spec-driven renderer: pages are described in data/spec.js (window.SPEC). No dependencies. */
const $=(s,r=document)=>r.querySelector(s), fm=n=>(n==null||n===""||isNaN(n))?"-":Number(n).toLocaleString("en-IN");
const F={int:v=>fm(Math.round(v)),dec1:v=>v==null||isNaN(v)?"-":Number(v).toFixed(1),dec0:v=>v==null||isNaN(v)?"-":Number(v).toFixed(0),pct1:v=>v==null||isNaN(v)?"-":Number(v).toFixed(1)+"%",pct0:v=>v==null||isNaN(v)?"-":Number(v).toFixed(0)+"%",dec2:v=>v==null||isNaN(v)?"-":Number(v).toFixed(2),num:v=>v==null||isNaN(v)?"-":(Number.isInteger(+v)?fm(v):(+v).toFixed(2)),signed:v=>(v>0?"+":"")+fm(Math.round(v)),text:v=>v==null?"":v};
const fmt=(k,v)=>(F[k]||F.int)(v);
function heat(h,v){if(!h||v==null||isNaN(v))return "";const good=h.invert?(v<=h.lo):(v>=h.hi),bad=h.invert?(v>=h.hi):(v<=h.lo);return good?"color:var(--green);font-weight:600":bad?"color:var(--red);font-weight:600":""}
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;")}
function kpis(items){return `<div class="kpis">${items.map(i=>`<div class="k ${i.tone||""}"><b>${i.value}</b><span>${i.label}</span>${i.note?`<small>${i.note}</small>`:""}</div>`).join("")}</div>`}
function hbars(w){const rows=w.rows,mx=w.max||Math.max(...rows.map(r=>r.value),1),f=w.fmt||"int";
 return rows.map(r=>`<div class="bar"><span title="${esc(r.label)}">${esc(r.label)}</span><div class="track"><div class="fill" style="width:${Math.min(100,100*r.value/mx)}%;background:${r.color||w.color||"var(--c1)"}"></div></div><span class="num">${fmt(f,r.value)}${r.sub?` <small style="color:var(--mute)">${esc(r.sub)}</small>`:""}</span></div>`).join("")}
function stackOne(parts){const t=parts.reduce((a,p)=>a+p.value,0)||1;
 return `<div class="stack">${parts.map(p=>`<i style="width:${100*p.value/t}%;background:${p.color}" title="${esc(p.label)}: ${p.value}"></i>`).join("")}</div><div class="leg">${parts.map(p=>`<span><u style="background:${p.color}"></u>${esc(p.label)}: ${fm(p.value)} (${(100*p.value/t).toFixed(0)}%)</span>`).join("")}</div>`}
function stacks(w){return w.groups.map(g=>`<b>${esc(g.name)}</b>${stackOne(g.parts)}`).join("")}
function line(w){const W=640,H=w.h||250,L=46,R=14,T=14,B=30,all=w.series.flatMap(s=>s.values.filter(v=>v!=null)),mn=w.min??0,mx=w.max??Math.max(...all)*1.08,n=w.labels.length,
 x=i=>L+(W-L-R)*i/Math.max(n-1,1),y=v=>T+(H-T-B)*(1-(v-mn)/(mx-mn||1));let g="";
 for(let k=0;k<=4;k++){const v=mn+(mx-mn)*k/4;g+=`<line x1="${L}" x2="${W-R}" y1="${y(v)}" y2="${y(v)}" stroke="var(--line)"/><text x="${L-6}" y="${y(v)+4}" text-anchor="end">${fm(Math.round(v))}</text>`}
 w.labels.forEach((l,i)=>{if(n<=7||i%Math.ceil(n/7)===0||i===n-1)g+=`<text x="${x(i)}" y="${H-8}" text-anchor="middle">${esc(l)}</text>`});
 w.series.forEach(s=>{const pts=s.values.map((v,i)=>v==null?null:[x(i),y(v)]).filter(Boolean);g+=`<polyline fill="none" stroke="${s.color}" stroke-width="2.2" points="${pts.map(p=>p.join(",")).join(" ")}"/>`+s.values.map((v,i)=>v==null?"":`<circle cx="${x(i)}" cy="${y(v)}" r="3" fill="${s.color}"><title>${esc(s.name)} ${esc(w.labels[i])}: ${fm(v)}</title></circle>`).join("")});
 return `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img">${g}</svg><div class="leg">${w.series.map(s=>`<span><u style="background:${s.color}"></u>${esc(s.name)}</span>`).join("")}</div>`}
let TID=0;
function table(w,host){const id="t"+(++TID);let sk=w.sort||w.cols[0].key,dir=w.dir??-1,q="";
 host.innerHTML=`<div class="ctl">${w.search?`<input placeholder="Search ${esc(w.search)}">`:""}<span class="note" style="margin:0">Click a heading to sort.</span></div><div class="scroll" ${w.maxh?`style="max-height:${w.maxh}px"`:""}><table><thead><tr></tr></thead><tbody></tbody></table></div>`;
 const draw=()=>{const d=w.rows.filter(r=>!q||String(r[w.cols[0].key]).toLowerCase().includes(q)).sort((a,b)=>dir*((a[sk]>b[sk])-(a[sk]<b[sk])));
  $("thead tr",host).innerHTML=w.cols.map(c=>`<th class="${c.fmt&&c.fmt!=="text"?"n":""}" data-k="${c.key}">${esc(c.label)}${c.key===sk?(dir<0?" ▼":" ▲"):""}</th>`).join("");
  $("tbody",host).innerHTML=d.map(r=>"<tr>"+w.cols.map(c=>`<td class="${c.fmt&&c.fmt!=="text"?"n":""}" style="${heat(c.heat,r[c.key])}">${esc(fmt(c.fmt||"text",r[c.key]))}</td>`).join("")+"</tr>").join("");
  host.querySelectorAll("th").forEach(h=>h.onclick=()=>{const k=h.dataset.k;dir=k===sk?-dir:-1;sk=k;draw()})};
 draw();const i=$("input",host);if(i)i.oninput=e=>{q=e.target.value.toLowerCase();draw()}}
function widget(w){const h=document.createElement("div");h.className="card";if(w.title)h.insertAdjacentHTML("beforeend",`<h2>${esc(w.title)}</h2>`);const b=document.createElement("div");h.appendChild(b);
 if(w.type==="hbars")b.innerHTML=hbars(w);else if(w.type==="stack")b.innerHTML=stackOne(w.parts);else if(w.type==="stacks")b.innerHTML=stacks(w);else if(w.type==="line")b.innerHTML=line(w);
 else if(w.type==="table")table(w,b);else if(w.type==="text")b.innerHTML=w.html;
 if(w.note)h.insertAdjacentHTML("beforeend",`<p class="note">${esc(w.note)}</p>`);return h}
function render(){const S=window.SPEC,pid=document.body.dataset.page||"index",P=S.project;
 const pages=[["index.html","Home"]].concat(S.pages.map(p=>[p.id+".html",p.nav||p.title]));
 document.body.insertAdjacentHTML("afterbegin",`<div class="top"><b>${esc(P.title)}</b>${pages.map(([h,t])=>`<a href="${h}" class="${h===pid+".html"?"on":""}">${esc(t)}</a>`).join("")}<button id="th">Theme</button></div><div class="wrap" id="app"></div>`);
 $("#th").onclick=()=>{const r=document.documentElement;r.dataset.theme=getComputedStyle(r).getPropertyValue("--bg").trim()==="#0f1c21"?"light":"dark"};
 const app=$("#app");
 if(pid==="index"){app.innerHTML=`<h1>${esc(P.title)}</h1><p class="sub">${P.subtitle}</p>${P.banner?`<div class="warn">${P.banner}</div>`:""}${P.kpis?kpis(P.kpis):""}<div class="cards">${S.pages.map(p=>`<a class="card" href="${p.id}.html"><h2>${esc(p.title)}</h2><p style="margin:0">${p.intro}</p><div>${(p.tags||[]).map(t=>`<span class="pill">${esc(t)}</span>`).join("")}</div></a>`).join("")}</div>`;return}
 const p=S.pages.find(x=>x.id===pid);app.innerHTML=`<h1>${esc(p.title)}</h1><p class="sub">${p.intro}</p>`;
 let buf=[];const flush=()=>{if(!buf.length)return;const g=document.createElement("div");g.className="grid";buf.forEach(x=>g.appendChild(x));app.appendChild(g);buf=[]};
 p.widgets.forEach(w=>{if(w.type==="kpis"){flush();app.insertAdjacentHTML("beforeend",kpis(w.items))}else if(w.type==="banner"){flush();app.insertAdjacentHTML("beforeend",`<div class="warn">${w.html}</div>`)}
  else if(w.w==="half"){buf.push(widget(w));if(buf.length===2)flush()}else{flush();app.appendChild(widget(w))}});flush();
 if(P.footer)app.insertAdjacentHTML("beforeend",`<p class="note">${P.footer}</p>`)}
document.addEventListener("DOMContentLoaded",render);
