import CoreRadio from 'core-radio';
import Topnav from '@/components/topnav';
import Modal from '@/components/modal';

export default {
  main: function() {

    document.addEventListener('click', e => {
      if(!e.target.dataset.event) return;
      let dataset = Object.assign({}, e.target.dataset);
      CoreRadio.publish(dataset.event, {e: e, dataset: dataset});
    });
    
    Topnav.main();
    Modal.main();
  }
};
