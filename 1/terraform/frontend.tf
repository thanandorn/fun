resource "kubernetes_deployment" "frontend" {
  metadata {
    name      = "frontend"
    namespace = kubernetes_namespace.main.metadata[0].name
    labels = {
      app = "frontend"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "frontend"
      }
    }

    template {
      metadata {
        labels = {
          app = "frontend"
        }
      }

      spec {
        container {
          image   = "library/busybox:1.29.3"
          name    = "frontend"
          command = ["/bin/sh", "-c"]
          args = [
            "while [ 1 ]; do sleep 2; echo $(date) - Frontend ; done"
          ]
        }
      }
    }
  }
}
