      SUBROUTINE ASYMTOP(j,itau,ntau,n,ac,eg)
      IMPLICIT REAL*4 (A-H, O-Z)
 
c
c     This subroutine has to be replaced with proper Ac and Eg values
c     for other C2v molecules.
c     These data are for the Pyridazine molecule with up to J=5(AXX= 0.262150E-04  BYY= 0.250400E-04 CZZ= 0.128070E-04)
c     The energies eg(i) are in the units of eV.
c
      DIMENSION eg(11) , ac(11,6,2) , itau(11) , ntau(11)

      DO ii = 1 , 11
        DO jj = 1 , 6
          DO kk = 1 , 2
            ac(ii,jj,kk) = 0.0
          END DO
        END DO
      END DO

      n = j + j + 1
      DO i = 1 , n
        ip = i
        ntau(i) = ip
        itau(i) = i - j - 1
      END DO
      IF ( j.NE.0 ) THEN
        IF ( j.EQ.2 ) THEN
          eg(1) = 0.102402E-03 
          eg(2) = 0.102483E-03 
          eg(3) = 0.139182E-03
          eg(4) = 0.142707E-03 
          eg(5) = 0.153846E-03
          ac(1,1,1) = -0.039592E0 
          ac(1,1,2) = 0.0 
          ac(1,3,1) = 0.999216E0 
          ac(1,3,2) = 0.0 
          ac(2,2,1) = 0.0 
          ac(2,2,2) = 1.000000E0 
          ac(3,3,1) = 0.0 
          ac(3,3,2) = 1.000000E0 
          ac(4,2,1) = 1.000000E0 
          ac(4,2,2) = 0.0 
          ac(5,1,1) = 0.999216E0 
          ac(5,1,2) = 0.0 
          ac(5,3,1) = 0.039592E0 
          ac(5,3,2) = 0.0 
          RETURN
        ELSE IF ( j.EQ.3 ) THEN
          eg(1) = 0.192093E-03 
          eg(2) = 0.192097E-03
          eg(3) = 0.255847E-03
          eg(4) = 0.256248E-03
          eg(5) = 0.291237E-03
          eg(6) = 0.298283E-03
          eg(7) = 0.307931E-03
          ac(1,2,1) = 0.0 
          ac(1,2,2) = -0.022956E0
          ac(1,4,1) = 0.0
          ac(1,4,2) = 0.999736E0
          ac(2,1,1) = -0.021433E0
          ac(2,1,2) = 0.0
          ac(2,3,1) = 0.999770E0
          ac(2,3,2) = 0.0
          ac(3,2,1) = -0.087712E0
          ac(3,2,2) = 0.0
          ac(3,4,1) = 0.996146E0
          ac(3,4,2) = 0.0
          ac(4,3,1) = 0.0
          ac(4,3,2) = 1.000000E0
          ac(5,2,1) = 0.0
          ac(5,2,2) = 0.999736E0
          ac(5,4,1) = 0.0
          ac(5,4,2) = 0.022956E0
          ac(6,1,1) = 0.999770E0
          ac(6,1,2) = 0.0
          ac(6,3,1) = 0.021433E0
          ac(6,3,2) = 0.0
          ac(7,2,1) = 0.996146E0
          ac(7,2,2) = 0.0
          ac(7,4,1) = 0.087712E0
          ac(7,4,2) = 0.0
          RETURN
        ELSE IF ( j.EQ.4 ) THEN
          eg(1) = 0.307359E-03 
          eg(2) = 0.307359E-03
          eg(3) = 0.396941E-03
          eg(4) = 0.396965E-03
          eg(5) = 0.460146E-03
          eg(6) = 0.461331E-03
          eg(7) = 0.494079E-03 
          eg(8) = 0.505805E-03
          eg(9) = 0.513735E-03
          ac(1,1,1) = 0.000777E0 
          ac(1,1,2) = 0.0
          ac(1,3,1) = -0.148707E0
          ac(1,3,2) = 0.0
          ac(1,5,1) = 0.988881E0
          ac(1,5,2) = 0.0
          ac(2,2,1) = 0.0
          ac(2,2,2) = -0.020195E0
          ac(2,4,1) = 0.0
          ac(2,4,2) = 0.999796E0
          ac(3,3,1) = 0.0
          ac(3,3,2) = -0.048061E0
          ac(3,5,1) = 0.0
          ac(3,5,2) = 0.998844E0
          ac(4,2,1) = -0.042884E0
          ac(4,2,2) = 0.0
          ac(4,4,1) = 0.999080E0
          ac(4,4,2) = 0.0
          
          ac(5,1,1) = -0.020234E0
          ac(5,1,2) = 0.0
          ac(5,3,1) = 0.988676E0
          ac(5,3,2) = 0.0
          ac(5,5,1) = 0.148692E0
          ac(5,5,2) = 0.0
          
          ac(6,2,1) = 0.0
          ac(6,2,2) = 0.999796E0
          ac(6,4,1) = 0.0
          ac(6,4,2) = 0.020195E0
          
          ac(7,3,1) = 0.0
          ac(7,3,2) = 0.998844E0
          ac(7,5,1) = 0.0
          ac(7,5,2) = 0.048061E0
          
          ac(8,2,1) = 0.999080E0
          ac(8,2,2) = 0.0
          ac(8,4,1) = 0.042884E0
          ac(8,4,2) = 0.0
          
          ac(9,1,1) = 0.999795E0
          ac(9,1,2) = 0.0
          ac(9,3,1) = 0.020125E0
          ac(9,3,2) = 0.0
          ac(9,5,1) = 0.002241E0
          ac(9,5,2) = 0.0
          RETURN
        ELSE IF ( j.EQ.5 ) THEN
          eg(1) = 0.448237E-03 
          eg(2) = 0.448237E-03
          eg(3) = 0.563454E-03
          eg(4) = 0.563455E-03
          eg(5) = 0.652901E-03
          eg(6) = 0.652998E-03
          eg(7) = 0.715091E-03
          eg(8) = 0.717785E-03
          eg(9) = 0.747807E-03
          eg(10) = 0.765335E-03
          eg(11) = 0.771520E-03
          
          ac(1,2,1) = 0.0 
          ac(1,2,2) = 0.000490E0
          ac(1,4,1) = 0.0
          ac(1,4,2) = -0.080483E0
          ac(1,6,1) = 0.0
          ac(1,6,2) = 0.996756E0
          
          ac(2,1,1) = 0.000462E0
          ac(2,1,2) = 0.0
          ac(2,3,1) = -0.067930E0
          ac(2,3,2) = 0.0
          ac(2,5,1) = 0.997690E0
          ac(2,5,2) = 0.0
          
          ac(3,2,1) = 0.002332E0
          ac(3,2,2) = 0.0
          ac(3,4,1) = -0.218480E0
          ac(3,4,2) = 0.0
          ac(3,6,1) = 0.975839E0
          ac(3,6,2) = 0.0
          
          ac(4,3,1) = 0.0
          ac(4,3,2) = -0.039592E0
          ac(4,5,1) = 0.0
          ac(4,5,2) = 0.999216E0
          
          ac(5,2,1) = 0.0
          ac(5,2,2) = -0.019220E0
          ac(5,4,1) = 0.0
          ac(5,4,2) = 0.996571E0
          ac(5,6,1) = 0.0
          ac(5,6,2) = 0.080477E0
          
          ac(6,1,1) = -0.019219E0
          ac(6,1,2) = 0.0
          ac(6,3,1) = 0.997505E0
          ac(6,3,2) = 0.0
          ac(6,5,1) = 0.067926E0
          ac(6,5,2) = 0.0
          
          ac(7,2,1) = -0.039774E0
          ac(7,2,2) = 0.0
          ac(7,4,1) = 0.975049E0
          ac(7,4,2) = 0.0
          ac(7,6,1) = 0.218399E0
          ac(7,6,2) = 0.0
          
          ac(8,3,1) = 0.0
          ac(8,3,2) = 0.999216E0
          ac(8,5,1) = 0.0
          ac(8,5,2) = 0.039592E0
          
          ac(9,2,1) = 0.0
          ac(9,2,2) = 0.999815E0
          ac(9,4,1) = 0.0
          ac(9,4,2) = 0.019197E0
          ac(9,6,1) = 0.0
          ac(9,6,2) = 0.001059E0
          
          ac(10,1,1) = 0.999815E0
          ac(10,1,2) = 0.0
          ac(10,3,1) = 0.019206E0
          ac(10,3,2) = 0.0
          ac(10,5,1) = 0.000844E0
          ac(10,5,2) = 0.0
          
          ac(11,2,1) = 0.999206E0
          ac(11,2,2) = 0.0
          ac(11,4,1) = 0.039322E0
          ac(11,4,2) = 0.0
          ac(11,6,1) = 0.006416E0
          ac(11,6,2) = 0.0
          RETURN 
        ELSE
          eg(1) = 0.378470E-04 
          eg(2) = 0.390220E-04
          eg(3) = 0.512550E-04
          ac(1,2,1) = 0.0 
          ac(1,2,2) = 1.000000E0
          ac(2,1,1) = 1.000000E0
          ac(2,1,2) = 0.0
          ac(3,2,1) = 1.000000E0
          ac(3,2,2) = 0.0
          RETURN
        END IF
      END IF
      eg(1) = 0.0
      ac(1,1,1) = 1.0
      ac(1,1,2) = 0.0

      RETURN
      END