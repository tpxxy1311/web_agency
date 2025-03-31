"use client"
import styles from "@/styles/components/navigation.module.scss"
import { 
    HomeOutlined, 
    TravelExploreOutlined, 
    CompareArrows, 
    DescriptionOutlined,
    CheckroomOutlined
} from "@mui/icons-material";
import Link from "next/link";
import { usePathname } from "next/navigation";

const MainNavigation = () => {
    const pathname = usePathname()
    return ( 
        <nav className={styles.navContainer}>
            <Link href="/" className={`${styles.linkContainer} ${pathname === '/' ? styles.active : ''}`}>
                <div className={styles.iconContainer}><HomeOutlined  sx={{ fontSize: 18 }} className={styles.icon}/></div> <p>Start</p>
            </Link>
            <Link href="/explore" className={`${styles.linkContainer} ${pathname === '/explore' ? styles.active : ''}`}>
            <div className={styles.iconContainer}><TravelExploreOutlined sx={{ fontSize: 18 }} className={styles.icon}/> </div> <p>Explore</p>
            </Link>
            <Link href="/compare" className={`${styles.linkContainer} ${pathname === '/compare' ? styles.active : ''}`}>
                <div className={styles.iconContainer}><CompareArrows sx={{ fontSize: 18 }} className={styles.icon}/></div> <p>Compare</p>
            </Link>
            <Link href="/combine" className={`${styles.linkContainer} ${pathname === '/combine' ? styles.active : ''}`}>
                <div className={styles.iconContainer}><CheckroomOutlined sx={{ fontSize: 18 }} className={styles.icon}/></div> <p>Combine</p>
            </Link>
            <Link href="/reports" className={`${styles.linkContainer} ${pathname === '/reports' ? styles.active : ''}`}>
                <div className={styles.iconContainer}><DescriptionOutlined sx={{ fontSize: 18 }} className={styles.icon}/></div> <p>Reports</p>
            </Link>
        </nav>
     );
}
 
export default MainNavigation;