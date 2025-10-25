// dashboard.js
(async function(){
  const profileCard = document.getElementById('profileCard');
  const analytics = document.getElementById('analytics');
  const riskScoreEl = document.getElementById('riskScore');
  const allocationEl = document.getElementById('allocation');
  const projectedEl = document.getElementById('projected');
  const portfolioList = document.getElementById('portfolioList');

  document.getElementById('editProfile').addEventListener('click', () => location.href = 'profile.html');
  document.getElementById('connectHuman').addEventListener('click', () => location.href = 'mailto:advisor@example.com?subject=Request%20Human%20Advisor');

  const profile = loadProfileFromLocal();
  if(!profile){ profileCard.innerText = 'No profile found. Create one at Profile.'; analytics.style.display = 'none'; return; }

  // show profile summary
  profileCard.innerHTML = `<div><strong>${profile.name}</strong><div class="muted">${profile.age} yrs${profile.income?(' • Income: '+inrFmt.format(profile.income)) : ' • Income: (hidden)'}</div></div>`;

  // fetch analytics from server
  try {
    const res = await fetch('/api/ai/recommendation', { method: 'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(profile) });
    if(!res.ok) throw new Error('server error');
    const json = await res.json();

    analytics.style.display = 'block';
    riskScoreEl.innerText = json.riskScore.toFixed(1);
    allocationEl.innerText = json.allocationLabel;
    projectedEl.innerText = inrFmt.format(json.projectedValue);

    portfolioList.innerHTML = json.recommendations.map(r=>`<div><strong>${r.asset}</strong>: ${r.pct}% — ${r.note}</div>`).join('');
  } catch(err){
    console.warn(err);
    analytics.style.display = 'none';
    profileCard.innerHTML += '<div class="muted">Unable to fetch AI recommendations (server may be offline). Showing local heuristics.</div>';
    // optionally compute local using same heuristics (omitted for brevity)
  }
})();





.