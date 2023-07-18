function onOpen() {
  var ui = DocumentApp.getUi();
  ui.createMenu('カスタムメニュー')
      .addItem('空白を削除する', 'removeSpaces')
      .addToUi();
}

function removeSpaces() {
  var body = DocumentApp.getActiveDocument().getBody();
  var paragraphs = body.getParagraphs();
  for (var i = 0; i < paragraphs.length; i++) {
    var text = paragraphs[i].editAsText();
    var textString = text.getText();
    var newTextString = textString.replace(/[ 　]/g, "");
    if (newTextString !== textString) {
      text.setText(newTextString);
    }
  }
}
