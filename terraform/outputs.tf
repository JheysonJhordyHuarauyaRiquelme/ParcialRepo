#IP pública de la instancia EC2 desplegada

output "kubernetes_node_public_ip" {
  description = "IP pública del nodo K3s"
  value       = aws_instance.k8s_node.public_ip
}
