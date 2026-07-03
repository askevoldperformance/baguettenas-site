(function () {
  function getISOWeek(date) {
    var d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
    var dayNum = d.getUTCDay() || 7;
    d.setUTCDate(d.getUTCDate() + 4 - dayNum);
    var yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    return Math.ceil(((d - yearStart) / 86400000 + 1) / 7);
  }

  function render() {
    var box = document.getElementById('ukens-baguett');
    var list = window.__BAGUETTES__;
    if (!box || !list || !list.length) return;

    var week = getISOWeek(new Date());
    var item = list[week % list.length];

    document.getElementById('ukens-baguett-name').textContent = item.name;
    document.getElementById('ukens-baguett-price').textContent = item.price;
    document.getElementById('ukens-baguett-allergens').textContent =
      'Allergener: ' + item.allergens;
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render);
  } else {
    render();
  }
})();
