// profile.js
(function(){
  const form = document.getElementById('profileForm');
  const ageEl = document.getElementById('age');
  const incomeLabel = document.getElementById('incomeLabel');
  const incomeEl = document.getElementById('income');
  const demoBtn = document.getElementById('demoBtn');

  const MAX_INCOME = 10000000; // 1 crore

  function toggleIncomeVisibility(){
    const age = Number(ageEl.value || 0);
    if(age > 0 && age < 18){
      incomeLabel.style.display = 'none';
    } else {
      incomeLabel.style.display = 'block';
    }
  }

  ageEl.addEventListener('change', toggleIncomeVisibility);

  incomeEl.addEventListener('change', () => {
    let v = Number(incomeEl.value || 0);
    if(v > MAX_INCOME){
      incomeEl.value = MAX_INCOME;
      alert('Monthly income capped at ₹1,00,00,000 (1 crore).');
    }
  });

  demoBtn.addEventListener('click', () => {
    document.getElementById('name').value = 'Asha Rao';
    ageEl.value = 28; toggleIncomeVisibility();
    incomeEl.value = 120000;
    document.getElementById('savings').value = 200000;
    document.getElementById('invest').value = 50000;
    document.getElementById('horizon').value = '5';
    document.getElementById('risk').value = 'medium';
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const profile = {
      name: document.getElementById('name').value.trim(),
      age: Number(document.getElementById('age').value || 0),
      income: Number(document.getElementById('income').value || 0),
      savings: Number(document.getElementById('savings').value || 0),
      invest: Number(document.getElementById('invest').value || 0),
      horizon: Number(document.getElementById('horizon').value || 5),
      risk: document.getElementById('risk').value
    };

    // apply client-side rules
    const p = ensureIncomeRules(profile);

    // save locally and send to backend
    saveProfileToLocal(p);

    try {
      const res = await fetch('/api/profile', {
        method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(p)
      });
      if(!res.ok) throw new Error('server error');
      // go to dashboard
      window.location.href = 'dashboard.html';
    } catch(err){
      console.warn(err);
      // still allow local flow
      window.location.href = 'dashboard.html';
    }
  });

  // toggle on load if profile exists
  (function init(){
    const saved = loadProfileFromLocal();
    if(saved){
      document.getElementById('name').value = saved.name || '';
      ageEl.value = saved.age || '';
      document.getElementById('savings').value = saved.savings || '';
      document.getElementById('invest').value = saved.invest || '';
      document.getElementById('horizon').value = saved.horizon || '5';
      document.getElementById('risk').value = saved.risk || 'medium';
      if(saved.income) incomeEl.value = saved.income;
      toggleIncomeVisibility();
    }
  })();
})();
