resource "helm_release" "mongodb" {
  name       = "mongodb"
  repository = "stable"
  chart      = "mongodb"
  namespace  = kubernetes_namespace.main.metadata[0].name
  keyring    = ""
  wait       = true

  set {
    name  = "image.tag"
    value = "4.2.4-debian-10-r0"
  }

  set {
    name  = "mongodbRootPassword"
    value = "secretPassword" # Dont you dare use this anywhere
  }

  set {
    name  = "mongodbUsername"
    value = "backend"
  }

  set {
    name  = "mongodbPassword"
    value = "password" #  Just dont.
  }

  set {
    name  = "mongodbDatabase"
    value = "backend"
  }
}

