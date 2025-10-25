// main.js - helper utilities used by pages

// format INR
const inrFmt = new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 });

function saveProfileToLocal(profile){
  localStorage.setItem('af_profile', JSON.stringify(profile));
}

function loadProfileFromLocal(){
  return JSON.parse(localStorage.getItem('af_profile') || 'null');
}

function ensureIncomeRules(profile){
  // enforce server & client same rule: cap income to 1 crore and hide for < 18
  const MAX_INCOME = 10000000; // 1,00,00,000 -> 1 crore
  if(profile.income && profile.income > MAX_INCOME) profile.income = MAX_INCOME;
  if(profile.age && profile.age < 18) profile.income = null;
  return profile;
}
