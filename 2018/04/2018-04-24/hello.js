document.addEventListener("DOMContentLoaded", function() {
  const btn = document.getElementById("clickme");
  btn.addEventListener("click", function() {
    const boxes = document.getElementById("boxes");

    boxes.addEventListener("click", function(e) {
      const el = e.target;
      const ob = { text: el.textContent, klass: el.className };
      console.table(ob);
    });

    const nums = [3, 5, 7];
    for (num of nums) {
      const box = document.createElement("div");
      const text = document.createTextNode(num);
      box.className = "box";
      box.appendChild(text);
      boxes.appendChild(box);
    }
  });
});
