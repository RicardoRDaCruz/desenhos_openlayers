var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
/**
 * @module ol/layer/VectorImage
 */
import BaseVectorLayer from './BaseVector.js';
import CanvasVectorImageLayerRenderer from '../renderer/canvas/VectorImageLayer.js';
import { assign } from '../obj.js';
/**
 * @template {import("../source/Vector.js").default} VectorSourceType
 * @typedef {Object} Options
 * @property {string} [className='ol-layer'] A CSS class name to set to the layer element.
 * @property {number} [opacity=1] Opacity (0, 1).
 * @property {boolean} [visible=true] Visibility.
 * @property {import("../extent.js").Extent} [extent] The bounding extent for layer rendering.  The layer will not be
 * rendered outside of this extent.
 * @property {number} [zIndex] The z-index for layer rendering.  At rendering time, the layers
 * will be ordered, first by Z-index and then by position. When `undefined`, a `zIndex` of 0 is assumed
 * for layers that are added to the map's `layers` collection, or `Infinity` when the layer's `setMap()`
 * method was used.
 * @property {number} [minResolution] The minimum resolution (inclusive) at which this layer will be
 * visible.
 * @property {number} [maxResolution] The maximum resolution (exclusive) below which this layer will
 * be visible.
 * @property {number} [minZoom] The minimum view zoom level (exclusive) above which this layer will be
 * visible.
 * @property {number} [maxZoom] The maximum view zoom level (inclusive) at which this layer will
 * be visible.
 * @property {import("../render.js").OrderFunction} [renderOrder] Render order. Function to be used when sorting
 * features before rendering. By default features are drawn in the order that they are created. Use
 * `null` to avoid the sort, but get an undefined draw order.
 * @property {number} [renderBuffer=100] The buffer in pixels around the viewport extent used by the
 * renderer when getting features from the vector source for the rendering or hit-detection.
 * Recommended value: the size of the largest symbol, line width or label.
 * @property {VectorSourceType} [source] Source.
 * @property {import("../PluggableMap.js").default} [map] Sets the layer as overlay on a map. The map will not manage
 * this layer in its layers collection, and the layer will be rendered on top. This is useful for
 * temporary layers. The standard way to add a layer to a map and have it managed by the map is to
 * use {@link import("../PluggableMap.js").default#addLayer map.addLayer()}.
 * @property {boolean} [declutter=false] Declutter images and text on this layer. The priority is defined
 * by the `zIndex` of the style and the render order of features. Higher z-index means higher priority.
 * Within the same z-index, a feature rendered before another has higher priority.
 * @property {import("../style/Style.js").StyleLike} [style] Layer style. See
 * {@link import("../style/Style.js").default the style docs} for the default style that will be used if
 * this is not defined.
 * @property {number} [imageRatio=1] Ratio by which the rendered extent should be larger than the
 * viewport extent. A larger ratio avoids cut images during panning, but will cause a decrease in performance.
 * @property {Object<string, *>} [properties] Arbitrary observable properties. Can be accessed with `#get()` and `#set()`.
 */
/**
 * @classdesc
 * Vector data that is rendered client-side.
 * Note that any property set in the options is set as a {@link module:ol/Object~BaseObject}
 * property on the layer object; for example, setting `title: 'My Title'` in the
 * options means that `title` is observable, and has get/set accessors.
 *
 * @template {import("../source/Vector.js").default} VectorSourceType
 * @extends {BaseVectorLayer<VectorSourceType>}
 * @api
 */
var VectorImageLayer = /** @class */ (function (_super) {
    __extends(VectorImageLayer, _super);
    /**
     * @param {Options<VectorSourceType>} [opt_options] Options.
     */
    function VectorImageLayer(opt_options) {
        var _this = this;
        var options = opt_options ? opt_options : {};
        var baseOptions = assign({}, options);
        delete baseOptions.imageRatio;
        _this = _super.call(this, baseOptions) || this;
        /**
         * @type {number}
         * @private
         */
        _this.imageRatio_ =
            options.imageRatio !== undefined ? options.imageRatio : 1;
        return _this;
    }
    /**
     * @return {number} Ratio between rendered extent size and viewport extent size.
     */
    VectorImageLayer.prototype.getImageRatio = function () {
        return this.imageRatio_;
    };
    /**
     * Create a renderer for this layer.
     * @return {import("../renderer/Layer.js").default} A layer renderer.
     */
    VectorImageLayer.prototype.createRenderer = function () {
        return new CanvasVectorImageLayerRenderer(this);
    };
    return VectorImageLayer;
}(BaseVectorLayer));
export default VectorImageLayer;
//# sourceMappingURL=VectorImage.js.map