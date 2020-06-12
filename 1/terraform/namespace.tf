resource "kubernetes_namespace" "main" {
  metadata {
    name = var.envname
  }
}
