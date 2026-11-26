const LABELS = { 1: "низький", 2: "середній", 3: "високий" };

function formatTask(task) {
  const mark = task.done === true ? "[x]" : "[ ]";
  return mark + " " + task.title + " (" + LABELS[task.priority] + ")";
}

module.exports = { formatTask };
