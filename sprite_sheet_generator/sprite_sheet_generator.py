def start():
  application = Krita.instance()
  currentDoc = application.activeDocument()
  activeWindow = application.activeWindow()
  view = activeWindow.activeView()


  w: int = currentDoc.width()
  h: int = currentDoc.height()
  selectedNodes = view.selectedNodes()
  numSelectedNodes : int = len(selectedNodes)
  print("w: {}, h: {}, total: {}".format(w,h, numSelectedNodes))

  # Create new document to store the spritesheet
  newDocument = application.createDocument(
    w*numSelectedNodes, 
    h, 
    "{}_spritesheet".format(currentDoc.name()), 
    currentDoc.colorModel(),
    currentDoc.colorDepth(),
    currentDoc.colorProfile(),
    currentDoc.resolution()
  )
  
  for idx, node in enumerate(selectedNodes):
    # Easy way, but not working, making some weird behaviours
    # newNode = currentDoc.createNode("{}_copy".format(node.name()), node.type())
    # dupe = node.duplicate()
    # added = newDocument.rootNode().addChildNode(dupe, None)

    # Clone layer data
    newNode = newDocument.createNode(node.name(), node.type())

    # Content of the layer, start from zero to ignore pixels out of the layer
    pixelData = node.pixelData(0,0,w,h)

    newNode.setPixelData(pixelData,0,0,w,h) # Write data to the new layer
    
    # Reposition node
    newNode.move(idx * w, 0)
    added = newDocument.rootNode().addChildNode(newNode, None)
    print("Added {}: {}".format(newNode.name(),added))
  
  activeWindow.addView(newDocument)
