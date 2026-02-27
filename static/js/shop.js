document.addEventListener('DOMContentLoaded', function () {
  const addButtons = document.querySelectorAll('.add-btn');
  const cartItemsEl = document.getElementById('cart-items');
  const cartTotalEl = document.getElementById('cart-total');
  const clearBtn = document.getElementById('clear-cart');
  const cartSummaryEl = document.getElementById('cart-summary');

  let cart = [];

  function renderCart() {
    cartItemsEl.innerHTML = '';
    let total = 0;
    cart.forEach((it, idx) => {
      const li = document.createElement('li');
      li.textContent = `${it.name} — $${it.price}`;
      const rm = document.createElement('button');
      rm.textContent = 'Remove';
      rm.style.marginLeft = '8px';
      rm.addEventListener('click', () => {
        cart.splice(idx, 1);
        saveCart();
        renderCart();
      });
      li.appendChild(rm);
      cartItemsEl.appendChild(li);
      total += parseFloat(it.price);
    });
    cartTotalEl.textContent = total.toFixed(2);
    if (cartSummaryEl) {
      cartSummaryEl.textContent = `Items: ${cart.length} — Total: $${total.toFixed(2)}`;
    }
  }

  function saveCart() {
    try {
      localStorage.setItem('coffee_cart', JSON.stringify(cart));
    } catch (e) {
      console.warn('Could not save cart to localStorage', e);
    }
  }

  function loadCart() {
    try {
      const raw = localStorage.getItem('coffee_cart');
      if (raw) {
        const parsed = JSON.parse(raw);
        if (Array.isArray(parsed)) {
          cart = parsed.map(it => ({ name: it.name, price: parseFloat(it.price) }));
        }
      }
    } catch (e) {
      console.warn('Could not load cart from localStorage', e);
    }
  }

  addButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const name = btn.dataset.name;
      const price = parseFloat(btn.dataset.price);
      cart.push({ name, price });
      saveCart();
      renderCart();
    });
  });

  clearBtn.addEventListener('click', () => {
    cart = [];
    saveCart();
    renderCart();
  });

  // load any persisted cart then render
  loadCart();
  renderCart();
});
