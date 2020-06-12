resource "kubernetes_deployment" "backend" {
  metadata {
    name      = "backend"
    namespace = kubernetes_namespace.main.metadata[0].name
    labels = {
      app = "backend"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "backend"
      }
    }

    template {
      metadata {
        labels = {
          app = "backend"
        }
      }

      spec {
        container {
          image   = "library/busybox:1.29.3"
          name    = "backend"
          command = ["/bin/sh", "-c"]
          args = [
            "while [ 1 ]; do sleep 2; echo $(date) - Backend ; done"
          ]
        }
      }
    }
  }
}
