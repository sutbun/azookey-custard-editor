from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')


def replace_once(old, new, label):
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly one match, got {count}')
    text = text.replace(old, new, 1)


replace_once(
    '<title>&lt;非公式&gt; azooKey Custom Keyboard Editor v3.5.2</title>',
    '<title>&lt;非公式&gt; azooKey Custom Keyboard Editor v3.6.0</title>',
    'document title version'
)
replace_once(
    '<h1>&lt;非公式&gt; azooKey Custom Keyboard Editor <span style="font-size:13px;color:#666;font-weight:500">v3.5.2</span></h1>',
    '<h1>&lt;非公式&gt; azooKey Custom Keyboard Editor <span style="font-size:13px;color:#666;font-weight:500">v3.6.0</span></h1>',
    'visible version'
)
replace_once(
    '.move-pad-center{\n  display:flex;',
    '.fine-move-label{display:block;margin:7px 0 4px}\n.move-pad-center{\n  display:flex;',
    'fine move label style'
)

old_move = '''            <div class="move-pad" aria-label="キーを1マス移動">
              <span></span>
              <button id="moveUpBtn" class="smallbtn move-pad-btn" title="上へ" aria-label="上へ">↑</button>
              <span></span>
              <button id="moveLeftBtn" class="smallbtn move-pad-btn" title="左へ" aria-label="左へ">←</button>
              <span class="move-pad-center" aria-hidden="true">·</span>
              <button id="moveRightBtn" class="smallbtn move-pad-btn" title="右へ" aria-label="右へ">→</button>
              <span></span>
              <button id="moveDownBtn" class="smallbtn move-pad-btn" title="下へ" aria-label="下へ">↓</button>
              <span></span>
            </div>'''
new_move = old_move + '''
            <span class="key-command-label fine-move-label">0.1微調整</span>
            <div id="fineMovePad" class="move-pad" aria-label="キーを0.1移動">
              <span></span>
              <button id="fineMoveUpBtn" class="smallbtn move-pad-btn" title="上へ0.1" aria-label="上へ0.1">↑</button>
              <span></span>
              <button id="fineMoveLeftBtn" class="smallbtn move-pad-btn" title="左へ0.1" aria-label="左へ0.1">←</button>
              <span class="move-pad-center" aria-hidden="true">·</span>
              <button id="fineMoveRightBtn" class="smallbtn move-pad-btn" title="右へ0.1" aria-label="右へ0.1">→</button>
              <span></span>
              <button id="fineMoveDownBtn" class="smallbtn move-pad-btn" title="下へ0.1" aria-label="下へ0.1">↓</button>
              <span></span>
            </div>'''
replace_once(old_move, new_move, 'fine move pad')

replacements = {
    '<input id="xInput" type="number" min="0" step="1">': '<input id="xInput" type="number" min="0" step="0.1">',
    '<input id="yInput" type="number" min="0" step="1">': '<input id="yInput" type="number" min="0" step="0.1">',
    '<input id="wInput" type="number" min="1" step="1">': '<input id="wInput" type="number" min="0.1" step="0.1">',
    '<input id="hInput" type="number" min="1" step="1">': '<input id="hInput" type="number" min="0.1" step="0.1">',
    '<input id="batchWidthInput" type="number" min="1" step="1" placeholder="例: 2">': '<input id="batchWidthInput" type="number" min="0.1" step="0.1" placeholder="例: 1.5">',
    '<input id="batchHeightInput" type="number" min="1" step="1" placeholder="例: 2">': '<input id="batchHeightInput" type="number" min="0.1" step="0.1" placeholder="例: 1.5">',
    '<input id="batchWidthDeltaInput" type="number" step="1" value="0" placeholder="例: 2 または -1">': '<input id="batchWidthDeltaInput" type="number" step="0.1" value="0" placeholder="例: 0.1 または -0.1">',
    '<input id="batchHeightDeltaInput" type="number" step="1" value="0" placeholder="例: 2 または -1">': '<input id="batchHeightDeltaInput" type="number" step="0.1" value="0" placeholder="例: 0.1 または -0.1">',
}
for old, new in replacements.items():
    replace_once(old, new, old)

old_batch_actions = '''        <div class="row-actions">
          <button id="applyBatchDeltaBtn" class="smallbtn">選択キーへ増減を適用</button>
          <button id="resetBatchDeltaBtn" class="smallbtn">増減値を0に戻す</button>
        </div>'''
new_batch_actions = old_batch_actions + '''
        <div class="row-actions" aria-label="選択キーの大きさを0.1微調整">
          <button id="decreaseBatchWidthBtn" class="smallbtn">幅 -0.1</button>
          <button id="increaseBatchWidthBtn" class="smallbtn">幅 +0.1</button>
          <button id="decreaseBatchHeightBtn" class="smallbtn">高さ -0.1</button>
          <button id="increaseBatchHeightBtn" class="smallbtn">高さ +0.1</button>
        </div>'''
replace_once(old_batch_actions, new_batch_actions, 'batch size fine controls')

replace_once(
    "  moveDown:{label:'キーを下へ移動',description:'選択キーを下へ1マス移動',run:()=>moveSelected(0,1)},\n  selectLeft:",
    "  moveDown:{label:'キーを下へ移動',description:'選択キーを下へ1マス移動',run:()=>moveSelected(0,1)},\n  fineMoveLeft:{label:'キーを左へ0.1移動',description:'選択キーを左へ0.1移動',run:()=>fineMoveSelected(-.1,0)},\n  fineMoveRight:{label:'キーを右へ0.1移動',description:'選択キーを右へ0.1移動',run:()=>fineMoveSelected(.1,0)},\n  fineMoveUp:{label:'キーを上へ0.1移動',description:'選択キーを上へ0.1移動',run:()=>fineMoveSelected(0,-.1)},\n  fineMoveDown:{label:'キーを下へ0.1移動',description:'選択キーを下へ0.1移動',run:()=>fineMoveSelected(0,.1)},\n  selectLeft:",
    'fine shortcut actions'
)
replace_once(
    "  {action:'moveRight',keys:'ArrowRight'},{action:'moveUp',keys:'ArrowUp'},{action:'moveDown',keys:'ArrowDown'},\n  {action:'selectLeft',keys:'Shift+ArrowLeft'},{action:'selectRight',keys:'Shift+ArrowRight'},\n  {action:'selectUp',keys:'Shift+ArrowUp'},{action:'selectDown',keys:'Shift+ArrowDown'},",
    "  {action:'moveRight',keys:'ArrowRight'},{action:'moveUp',keys:'ArrowUp'},{action:'moveDown',keys:'ArrowDown'},\n  {action:'fineMoveLeft',keys:'Shift+ArrowLeft'},{action:'fineMoveRight',keys:'Shift+ArrowRight'},\n  {action:'fineMoveUp',keys:'Shift+ArrowUp'},{action:'fineMoveDown',keys:'Shift+ArrowDown'},\n  {action:'selectLeft',keys:'Alt+ArrowLeft'},{action:'selectRight',keys:'Alt+ArrowRight'},\n  {action:'selectUp',keys:'Alt+ArrowUp'},{action:'selectDown',keys:'Alt+ArrowDown'},",
    'default directional shortcuts'
)

marker = '\n\n</script>\n\n\n\n</body>'
if text.count(marker) != 1:
    raise SystemExit(f'final script marker: expected 1, got {text.count(marker)}')

fractional_js = r'''

// ===== v3.6.0: official fractional grid_fit coordinates / sizes =====
const GRID_FIT_MIN_SIZE = 0.1;
const GRID_FINE_STEP = 0.1;

function normalizeGridNumber(value) {
  const number = Number(value);
  if (!Number.isFinite(number)) return 0;
  return Number(number.toFixed(9));
}

const moveSelectedBeforeFractionalGrid = moveSelected;
moveSelected = function(dx, dy) {
  if (isGridScrollLayout()) return moveSelectedBeforeFractionalGrid(dx, dy);
  const items = selectedItems();
  if (!items.length) return;
  mutate(() => items.forEach(item => {
    const s = item.specifier || (item.specifier = {x:0,y:0,width:1,height:1});
    s.x = normalizeGridNumber(Math.max(0, Number(s.x || 0) + dx));
    s.y = normalizeGridNumber(Math.max(0, Number(s.y || 0) + dy));
  }));
};

function fineMoveSelected(dx, dy) {
  if (isGridScrollLayout()) {
    setStatus('0.1微調整はgrid_fitで使用できます。', 'warn');
    return;
  }
  moveSelected(dx, dy);
}

const fineDirections = {
  fineMoveLeftBtn:[-GRID_FINE_STEP,0], fineMoveRightBtn:[GRID_FINE_STEP,0],
  fineMoveUpBtn:[0,-GRID_FINE_STEP], fineMoveDownBtn:[0,GRID_FINE_STEP]
};
Object.entries(fineDirections).forEach(([id,[dx,dy]]) => {
  document.getElementById(id)?.addEventListener('click', () => fineMoveSelected(dx,dy));
});

const shiftedMoveDirections = {
  moveLeftBtn:[-GRID_FINE_STEP,0], moveRightBtn:[GRID_FINE_STEP,0],
  moveUpBtn:[0,-GRID_FINE_STEP], moveDownBtn:[0,GRID_FINE_STEP]
};
Object.entries(shiftedMoveDirections).forEach(([id,[dx,dy]]) => {
  document.getElementById(id)?.addEventListener('click', event => {
    if (!event.shiftKey || isGridScrollLayout()) return;
    event.preventDefault();
    event.stopImmediatePropagation();
    fineMoveSelected(dx,dy);
  }, true);
});

function installFractionalSpecifierInput(input, key, min) {
  input.addEventListener('change', event => {
    if (isGridScrollLayout()) return;
    event.stopImmediatePropagation();
    const item = selected();
    if (!item) return;
    const value = Number(input.value);
    if (!Number.isFinite(value)) {
      populateForm();
      setStatus(`${key} は数値で入力してください。`, 'warn');
      return;
    }
    mutate(() => {
      const s = item.specifier || (item.specifier = {x:0,y:0,width:1,height:1});
      s[key] = Math.max(min, value);
    });
  }, true);
}
installFractionalSpecifierInput(xInput, 'x', 0);
installFractionalSpecifierInput(yInput, 'y', 0);
installFractionalSpecifierInput(wInput, 'width', GRID_FIT_MIN_SIZE);
installFractionalSpecifierInput(hInput, 'height', GRID_FIT_MIN_SIZE);

function replaceButtonWithoutLegacyHandlers(id) {
  const oldButton = document.getElementById(id);
  if (!oldButton) return null;
  const newButton = oldButton.cloneNode(true);
  oldButton.replaceWith(newButton);
  return newButton;
}

replaceButtonWithoutLegacyHandlers('applyBatchSizeBtn')?.addEventListener('click', () => {
  const items = selectedItems();
  if (!items.length) return setStatus('大きさを変更するキーを選択してください。', 'warn');
  const widthRaw = batchWidthInput.value.trim();
  const heightRaw = batchHeightInput.value.trim();
  if (!widthRaw && !heightRaw) return setStatus('幅または高さを入力してください。', 'warn');
  const width = widthRaw ? Number(widthRaw) : null;
  const height = heightRaw ? Number(heightRaw) : null;
  if ((width !== null && (!Number.isFinite(width) || width < GRID_FIT_MIN_SIZE)) ||
      (height !== null && (!Number.isFinite(height) || height < GRID_FIT_MIN_SIZE))) {
    return setStatus('幅と高さは0.1以上の数値で入力してください。', 'warn');
  }
  mutate(() => items.forEach(item => {
    const s = item.specifier || (item.specifier = {x:0,y:0,width:1,height:1});
    if (width !== null) s.width = width;
    if (height !== null) s.height = height;
  }));
  setStatus(`${items.length}個のキーの大きさを変更しました。`);
});

replaceButtonWithoutLegacyHandlers('applyBatchDeltaBtn')?.addEventListener('click', () => {
  const items = selectedItems();
  if (!items.length) return setStatus('大きさを変更するキーを選択してください。', 'warn');
  const dw = Number(batchWidthDeltaInput.value || 0);
  const dh = Number(batchHeightDeltaInput.value || 0);
  if (!Number.isFinite(dw) || !Number.isFinite(dh)) return setStatus('増減値は数値で入力してください。', 'warn');
  if (dw === 0 && dh === 0) return setStatus('幅または高さの増減値を入力してください。', 'warn');
  const invalid = items.some(item => {
    const s = item.specifier || {};
    return Number(s.width || 1) + dw < GRID_FIT_MIN_SIZE - 1e-9 ||
      Number(s.height || 1) + dh < GRID_FIT_MIN_SIZE - 1e-9;
  });
  if (invalid) return setStatus('変更後の幅または高さが0.1未満になるキーがあります。', 'warn');
  mutate(() => items.forEach(item => {
    const s = item.specifier || (item.specifier = {x:0,y:0,width:1,height:1});
    s.width = normalizeGridNumber(Number(s.width || 1) + dw);
    s.height = normalizeGridNumber(Number(s.height || 1) + dh);
  }));
  setStatus(`${items.length}個のキーへ、幅 ${dw>=0?'+':''}${dw}・高さ ${dh>=0?'+':''}${dh} を適用しました。`);
});

function adjustSelectedSize(axis, delta) {
  if (isGridScrollLayout()) return;
  const items = selectedItems();
  if (!items.length) return setStatus('大きさを変更するキーを選択してください。', 'warn');
  const invalid = items.some(item => Number(item.specifier?.[axis] || 1) + delta < GRID_FIT_MIN_SIZE - 1e-9);
  if (invalid) return setStatus('変更後の幅または高さが0.1未満になるキーがあります。', 'warn');
  mutate(() => items.forEach(item => {
    const s = item.specifier || (item.specifier = {x:0,y:0,width:1,height:1});
    s[axis] = normalizeGridNumber(Number(s[axis] || 1) + delta);
  }));
  const label = axis === 'width' ? '幅' : '高さ';
  setStatus(`${items.length}個のキーの${label}を ${delta>=0?'+':''}${delta} 変更しました。`);
}

document.getElementById('decreaseBatchWidthBtn')?.addEventListener('click', () => adjustSelectedSize('width', -GRID_FINE_STEP));
document.getElementById('increaseBatchWidthBtn')?.addEventListener('click', () => adjustSelectedSize('width', GRID_FINE_STEP));
document.getElementById('decreaseBatchHeightBtn')?.addEventListener('click', () => adjustSelectedSize('height', -GRID_FINE_STEP));
document.getElementById('increaseBatchHeightBtn')?.addEventListener('click', () => adjustSelectedSize('height', GRID_FINE_STEP));

const validSelectedKeyObjectBeforeFractionalGrid = validSelectedKeyObject;
validSelectedKeyObject = function(obj) {
  if (isGridScrollLayout()) return validSelectedKeyObjectBeforeFractionalGrid(obj);
  if (!obj || typeof obj !== 'object' || Array.isArray(obj)) return 'キーはJSONオブジェクトである必要があります。';
  if (!obj.specifier || typeof obj.specifier !== 'object') return 'specifier がありません。';
  for (const name of ['x','y','width','height']) {
    if (typeof obj.specifier[name] !== 'number' || !Number.isFinite(obj.specifier[name])) return `specifier.${name} は数値にしてください。`;
  }
  if (obj.specifier.x < 0 || obj.specifier.y < 0) return 'x と y は0以上にしてください。';
  if (obj.specifier.width < GRID_FIT_MIN_SIZE || obj.specifier.height < GRID_FIT_MIN_SIZE) return 'width と height は0.1以上にしてください。';
  if (obj.key_type !== 'custom' && obj.key_type !== 'system') return 'key_type は custom または system にしてください。';
  if (!obj.key || typeof obj.key !== 'object' || Array.isArray(obj.key)) return 'key がありません。';
  return '';
};

const validateBeforeFractionalGrid = validate;
validate = function() {
  if (isGridScrollLayout()) return validateBeforeFractionalGrid();
  const issues = [], ks = keys();
  for (let i=0; i<ks.length; i++) {
    const sa = ks[i].specifier || {};
    if (Number(sa.width || 0) < GRID_FIT_MIN_SIZE || Number(sa.height || 0) < GRID_FIT_MIN_SIZE) issues.push(`#${i}: 幅または高さが0.1未満です`);
    for (let j=i+1; j<ks.length; j++) {
      const sb = ks[j].specifier || {};
      const overlap = Number(sa.x || 0) < Number(sb.x || 0) + Number(sb.width || 1) &&
        Number(sa.x || 0) + Number(sa.width || 1) > Number(sb.x || 0) &&
        Number(sa.y || 0) < Number(sb.y || 0) + Number(sb.height || 1) &&
        Number(sa.y || 0) + Number(sa.height || 1) > Number(sb.y || 0);
      if (overlap) issues.push(`#${i} と #${j} が重なっています`);
    }
  }
  if (issues.length) renderWarningBox('確認してください', issues.slice(0,12), Math.max(0,issues.length-12));
  else renderWarningBox('', []);
  return issues;
};

selectionNavPoint = function(item, index) {
  if (isGridScrollLayout()) {
    const layout = scrollLayout();
    if (layout.direction === 'horizontal') {
      const rows = Math.max(1, Math.floor(Number(layout.column_count) || 1));
      return {x:Math.floor(index/rows), y:index%rows};
    }
    const cols = Math.max(1, Math.floor(Number(layout.row_count) || 1));
    return {x:index%cols, y:Math.floor(index/cols)};
  }
  const s = item?.specifier || {};
  return {
    x:Number(s.x || 0) + Math.max(GRID_FIT_MIN_SIZE, Number(s.width || 1))/2,
    y:Number(s.y || 0) + Math.max(GRID_FIT_MIN_SIZE, Number(s.height || 1))/2
  };
};

const oldSelectionShortcutDefaults = {
  selectLeft:'Shift+ArrowLeft', selectRight:'Shift+ArrowRight',
  selectUp:'Shift+ArrowUp', selectDown:'Shift+ArrowDown'
};
const newSelectionShortcutDefaults = {
  selectLeft:'Alt+ArrowLeft', selectRight:'Alt+ArrowRight',
  selectUp:'Alt+ArrowUp', selectDown:'Alt+ArrowDown'
};
const fineShortcutDefaults = {
  fineMoveLeft:'Shift+ArrowLeft', fineMoveRight:'Shift+ArrowRight',
  fineMoveUp:'Shift+ArrowUp', fineMoveDown:'Shift+ArrowDown'
};
const usesCompleteOldSelectionDefault = Object.entries(oldSelectionShortcutDefaults).every(([action,key]) =>
  shortcuts.some(item => item.action === action && normalizeShortcutString(item.keys) === key)
);
if (usesCompleteOldSelectionDefault) {
  Object.entries(newSelectionShortcutDefaults).forEach(([action,key]) => {
    const item = shortcuts.find(entry => entry.action === action);
    if (item) item.keys = key;
  });
} else {
  Object.entries(fineShortcutDefaults).forEach(([action,key]) => {
    const fineItem = shortcuts.find(entry => entry.action === action);
    if (!fineItem || normalizeShortcutString(fineItem.keys) !== key) return;
    const conflict = shortcuts.some(entry => entry !== fineItem && normalizeShortcutString(entry.keys) === key);
    if (conflict) fineItem.keys = '';
  });
}
localStorage.setItem(SHORTCUT_STORAGE, JSON.stringify(shortcuts));

const updateScrollSpecificUiBeforeFractionalGrid = updateScrollSpecificUi;
updateScrollSpecificUi = function() {
  updateScrollSpecificUiBeforeFractionalGrid();
  const finePad = document.getElementById('fineMovePad');
  const fineLabel = document.querySelector('.fine-move-label');
  const hidden = isGridScrollLayout();
  if (finePad) finePad.hidden = hidden;
  if (fineLabel) fineLabel.hidden = hidden;
};

updateScrollSpecificUi();
render();
populateForm();
'''

text = text.replace(marker, fractional_js + marker, 1)
path.write_text(text, encoding='utf-8')
