# MRI image reconstrucction using deep learning.
## Accelerated Magnetic resonance image(MRI) reconstruction using squeeze and excitation based residual blocks with cyclic loss and clinical validation of various MRI scan types
![image](https://github.com/user-attachments/assets/daa62e01-f715-487a-b75b-741049d84141)
Figure 1: A comprehensive perspective of the proposed network structure that encompasses a cyclic loss
### ABSTRACT
Background: Accelerated MRI image reconstruction has emerged as a prominent area of interest of research that aims to overcome the time constraints that are associated with traditional MRI acquisitions. The focus of this field is to reduce scan times while maintaining image quality by utilizing under sampling techniques. Several algorithms have been developed to tackle this challenge, employing different under sampling rates to achieve faster imaging protocols.
Methodology: In this present work, we introduce an approach that employs Generative Adversarial Networks (GANs) to accelerate the MRI image reconstruction. The generator  in this approach makes use of a Convolution layer that has a kernel size of 1, which in turn facilitates the identification of complicated relationships between the channels present in the feature map. The importance of each channel within the feature map is determined in a channel-wise manner using a Squeeze and Excitation block following this. Meanwhile, the discriminator utilized in this work employs a Patch GAN architecture. It also employs a cyclic loss mechanism that ensures the accuracy of the reconstruction.
Results: The SSIM was discovered to be 0.962 and the pSNR was calculated to be 33.42 after conducting a comprehensive analysis with various MRI scan types that includes T1 weighted, T2 weighted, Susceptibility weighted imaging (SWI), Diffusion-weighted imaging (DWI) using an echo-planar imaging two-dimensional (EP2D) which was acquired. The model was trained separately with the above different types of MRI scans.
Conclusion: The generative model has demonstrated its capacity to acquire knowledge across varied under sampling masks, thereby facilitating the acceleration of MRI image reconstruction. Additionally, this research has served to substantiate the efficacy of this approach across various diagnostic scan types.
### RESULTS
![image](https://github.com/user-attachments/assets/68ecb123-c316-459b-abc2-3c0bf5884e6e)
Figure 2: Ground truth, Zero-filled image and model predicted image along with error map for the comparison of model with two different under sampling mask Gaussian and Cartesian with 20% sampling rate. Corresponding SSIM and pSNR are mentioned.
### REPORT
https://docs.google.com/document/d/1UBEjwOkW8aK75dgP3dF9hHSqtrP2eBSv7gXqsL3mVCA/edit?usp=drivesdk
