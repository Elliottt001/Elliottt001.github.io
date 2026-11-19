// A small mouse-following tilt. Navigation remains an ordinary link.
(() => {
  const canTilt = window.matchMedia("(hover: hover) and (pointer: fine)");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const findCard = (target) => target instanceof Element ? target.closest(".ns-elsewhere__link") : null;

  document.addEventListener("pointermove", (event) => {
    const card = findCard(event.target);
    if (!card || event.pointerType !== "mouse" || !canTilt.matches || reduceMotion.matches) return;
    const box = card.getBoundingClientRect();
    const x = Math.max(0, Math.min(1, (event.clientX - box.left) / box.width));
    const y = Math.max(0, Math.min(1, (event.clientY - box.top) / box.height));
    card.style.setProperty("--wander-rx", `${(0.5 - y) * 3}deg`);
    card.style.setProperty("--wander-ry", `${(x - 0.5) * 3}deg`);
  });

  document.addEventListener("pointerout", (event) => {
    const card = findCard(event.target);
    if (!card || card.contains(event.relatedTarget)) return;
    card.style.removeProperty("--wander-rx");
    card.style.removeProperty("--wander-ry");
  });
})();
